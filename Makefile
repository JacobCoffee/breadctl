.PHONY: help install install-dev lint fmt ty test bench clean all build-python init-submodule

help: ## Show this help message
	@echo "Available targets:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

init-submodule: ## Initialize CPython submodule
	@if [ ! -d "cpython-lazy" ] || [ ! -d "cpython-lazy/.git" ]; then \
		echo "📦 Initializing cpython-lazy submodule..."; \
		if [ ! -f ".gitmodules" ]; then \
			echo "⚠️  .gitmodules not found, adding submodule..."; \
			git submodule add -b lazy https://github.com/LazyImportsCabal/cpython.git cpython-lazy; \
		fi; \
		git submodule update --init --recursive; \
		if [ -d "cpython-lazy" ]; then \
			echo "✅ Submodule initialized!"; \
		else \
			echo "❌ Failed to initialize submodule"; \
			echo "   Try: git submodule add -b lazy https://github.com/LazyImportsCabal/cpython.git cpython-lazy"; \
			exit 1; \
		fi; \
	else \
		echo "✅ Submodule already initialized"; \
	fi

build-python: init-submodule ## Build custom CPython 3.15 with PEP 810 support
	@echo "🐍 Building CPython 3.15 with PEP 810 support..."
	@echo "ℹ️  Required dependencies: gettext, openssl@3, xz, zstd"
	@echo "   macOS: brew install gettext openssl@3 xz zstd"
	@echo ""
	cd cpython-lazy && \
		if [ "$$(uname -s)" = "Darwin" ] && [ "$$(uname -m)" = "arm64" ]; then \
			export PATH="/opt/homebrew/opt/gettext/bin:$$PATH"; \
			export LDFLAGS="-L/opt/homebrew/opt/gettext/lib -L/opt/homebrew/opt/openssl@3/lib"; \
			export CPPFLAGS="-I/opt/homebrew/opt/gettext/include -I/opt/homebrew/opt/openssl@3/include"; \
			export PKG_CONFIG_PATH="/opt/homebrew/opt/gettext/lib/pkgconfig:/opt/homebrew/opt/openssl@3/lib/pkgconfig"; \
		fi && \
		./configure --with-pydebug --enable-optimizations --with-lto --prefix=$(shell pwd) && \
		make -j$(shell nproc 2>/dev/null || sysctl -n hw.ncpu 2>/dev/null || echo 4) && \
		make install
	@echo "✅ Python built successfully!"
	@echo "   Location: ./bin/python3.15"
	@echo ""
	@echo "⚠️Note⚠️: This includes LTO & Optimizations :)"
	@echo ""
	@echo "Updating .python-version..."
	@echo "./bin/python3.15" > .python-version
	@echo ""
	@echo "Verify with:"
	@echo "  ./bin/python3.15 --version"
	@echo "  ./bin/python3.15 -c 'lazy import sys; print(\"PEP 810 works!\")'"

install: ## Install project dependencies
	uv sync

upgrade: ## Upgrade dependencies
	uv lock --upgrade

lint: ## Run ruff linter
	uv run ruff check --fix --unsafe-fixes src/ tests/

fmt: ## Format code with ruff
	uv run ruff format src/ tests/

ty: ## Run type checking with ty
	uv run ty check src/

test: ## Run pytest tests
	uv run pytest

ci:  ty lint fmt test  ## Run all CI checks

bench-clean: ## Clear all benchmark results and charts
	@echo "🧹 Cleaning benchmark results..."
	@rm -f benchmarks/benchmark-*.md
	@rm -f benchmarks/*.png
	@echo "✅ Benchmark directory cleaned"

bench-all: bench-clean bench bench-full bench-verbose bench-plot bench-format ## Run complete benchmark suite with fresh results

bench: ## Run comprehensive benchmark for all variants (cappa, click, cyclopts)
	@echo "🔥 Comprehensive Benchmark: All CLI Variants"
	@echo "Requires: hyperfine >= 1.12 (brew install hyperfine)"
	@echo ""
	@echo "# breadctl Benchmark Results" > benchmarks/benchmark-results.md
	@echo "" >> benchmarks/benchmark-results.md
	@echo "Generated: $$(date)" >> benchmarks/benchmark-results.md
	@echo "" >> benchmarks/benchmark-results.md
	@echo "## CLI Framework Comparison (--help command)" >> benchmarks/benchmark-results.md
	@echo "" >> benchmarks/benchmark-results.md
	hyperfine --warmup 3 --runs 10 \
		--export-markdown benchmarks/benchmark-help.md \
		"uv run breadctl --help" \
		"uv run breadctl-lazy --help" \
		"uv run breadctl-click --help" \
		"uv run breadctl-click-lazy --help" \
		"uv run breadctl-cyclopts --help" \
		"uv run breadctl-cyclopts-lazy --help"
	@tail -n +1 benchmarks/benchmark-help.md >> benchmarks/benchmark-results.md
	@rm benchmarks/benchmark-help.md
	@echo ""
	@$(MAKE) bench-cappa-append
	@$(MAKE) bench-format
	@echo ""
	@echo "✅ Results saved to benchmarks/benchmark-results.md"

bench-cappa-append: ## Internal: Append cappa detailed results to benchmark-results.md
	@echo "## Full matrix with all subcommands" >> benchmarks/benchmark-results.md
	@echo "" >> benchmarks/benchmark-results.md
	@hyperfine --warmup 3 --runs 10 \
		--export-markdown benchmarks/benchmark-subcommands.md \
		"uv run breadctl --help" \
		"uv run breadctl-lazy --help" \
		"uv run breadctl bake" \
		"uv run breadctl-lazy bake" \
		"uv run breadctl deliver" \
		"uv run breadctl-lazy deliver" \
		"uv run breadctl inventory" \
		"uv run breadctl-lazy inventory"
	@tail -n +1 benchmarks/benchmark-subcommands.md >> benchmarks/benchmark-results.md
	@echo "" >> benchmarks/benchmark-results.md
	@echo "## Using \`python -c 'import breadctl.{normal,lazy}'\`" >> benchmarks/benchmark-results.md
	@echo "" >> benchmarks/benchmark-results.md
	@hyperfine --warmup 3 --runs 10 \
		--export-markdown benchmarks/benchmark-imports.md \
		"uv run python -c 'import breadctl_cappa.normal'" \
		"uv run python -c 'import breadctl_cappa.lazy'"
	@tail -n +1 benchmarks/benchmark-imports.md >> benchmarks/benchmark-results.md
	@rm benchmarks/benchmark-subcommands.md benchmarks/benchmark-imports.md

bench-full: ## Run comprehensive benchmark across all variants and commands
	@echo "🔥 Full Benchmark Matrix (All Variants × All Commands)"
	@echo ""
	@echo "## Full Matrix: All Variants × bake command" > benchmarks/benchmark-full-matrix.md
	@echo "" >> benchmarks/benchmark-full-matrix.md
	hyperfine --warmup 3 --runs 10 \
		--export-markdown benchmarks/benchmark-bake.md \
		"uv run breadctl bake" \
		"uv run breadctl-lazy bake" \
		"uv run breadctl-click bake" \
		"uv run breadctl-click-lazy bake" \
		"uv run breadctl-cyclopts bake" \
		"uv run breadctl-cyclopts-lazy bake"
	@tail -n +1 benchmarks/benchmark-bake.md >> benchmarks/benchmark-full-matrix.md
	@echo "" >> benchmarks/benchmark-full-matrix.md
	@echo "## Full Matrix: All Variants × deliver command" >> benchmarks/benchmark-full-matrix.md
	@echo "" >> benchmarks/benchmark-full-matrix.md
	hyperfine --warmup 3 --runs 10 \
		--export-markdown benchmarks/benchmark-deliver.md \
		"uv run breadctl deliver" \
		"uv run breadctl-lazy deliver" \
		"uv run breadctl-click deliver" \
		"uv run breadctl-click-lazy deliver" \
		"uv run breadctl-cyclopts deliver" \
		"uv run breadctl-cyclopts-lazy deliver"
	@tail -n +1 benchmarks/benchmark-deliver.md >> benchmarks/benchmark-full-matrix.md
	@echo "" >> benchmarks/benchmark-full-matrix.md
	@echo "## Full Matrix: All Variants × inventory command" >> benchmarks/benchmark-full-matrix.md
	@echo "" >> benchmarks/benchmark-full-matrix.md
	hyperfine --warmup 3 --runs 10 \
		--export-markdown benchmarks/benchmark-inventory.md \
		"uv run breadctl inventory" \
		"uv run breadctl-lazy inventory" \
		"uv run breadctl-click inventory" \
		"uv run breadctl-click-lazy inventory" \
		"uv run breadctl-cyclopts inventory" \
		"uv run breadctl-cyclopts-lazy inventory"
	@tail -n +1 benchmarks/benchmark-inventory.md >> benchmarks/benchmark-full-matrix.md
	@rm benchmarks/benchmark-bake.md benchmarks/benchmark-deliver.md benchmarks/benchmark-inventory.md
	@$(MAKE) bench-format
	@echo ""
	@echo "✅ Results saved to benchmarks/benchmark-full-matrix.md"

bench-verbose: ## Detailed benchmark with import time tracing
	@echo "" >> benchmarks/benchmark-verbose.md
	@echo "## Import time analysis (normal)" >> benchmarks/benchmark-verbose.md
	@echo "" >> benchmarks/benchmark-verbose.md
	@echo '```' >> benchmarks/benchmark-verbose.md
	@{ uv run python -X importtime -c "import breadctl.normal" 2>&1; } >> benchmarks/benchmark-verbose.md
	@echo '```' >> benchmarks/benchmark-verbose.md
	@echo "" >> benchmarks/benchmark-verbose.md
	@echo "## Import time analysis (lazy)" >> benchmarks/benchmark-verbose.md
	@echo "" >> benchmarks/benchmark-verbose.md
	@echo '```' >> benchmarks/benchmark-verbose.md
	@{ uv run python -X importtime -c "import breadctl.lazy" 2>&1; } >> benchmarks/benchmark-verbose.md
	@echo '```' >> benchmarks/benchmark-verbose.md
	@echo ""
	@echo "Detailed import traces appended to benchmarks/benchmark-verbose.md"

bench-format: ## Internal: Format markdown tables in benchmark results
	@# Remove empty table rows (rows with only pipes and spaces/dashes)
	@for file in benchmarks/benchmark-*.md; do \
		if [ -f "$$file" ]; then \
			sed -i.bak '/^|[[:space:]]*|[[:space:]]*|[[:space:]]*|[[:space:]]*|[[:space:]]*|$$/d' "$$file" && rm -f "$$file.bak"; \
		fi; \
	done

bench-plot: ## Generate visualization charts from benchmark results
	@echo "📊 Generating benchmark charts..."
	@echo "Note: Using Python 3.13 via uv (numpy doesn't support 3.15 yet)"
	@echo "Charts will be saved to benchmarks/"
	@uv run --no-project --python 3.13 --with matplotlib --with numpy python scripts/plot_benchmarks.py

clean: ## Remove cache and build artifacts
	rm -rf .pytest_cache .ruff_cache __pycache__ .coverage htmlcov
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name "__pycache__" -exec rm -rf {} +
