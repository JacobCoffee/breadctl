.PHONY: help install install-dev lint fmt ty test bench clean all

help: ## Show this help message
	@echo "Available targets:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

install: ## Install project
	uv sync

upgrade: ## Upgrade dependencies
	uv lock --upgrade

lint: ## Run ruff linter
	uv run ruff check src/ tests/

fmt: ## Format code with ruff
	uv run ruff format src/ tests/
	uv run ruff check --fix src/ tests/

ty: ## Run type checking with ty
	uv run ty check src/

test: ## Run pytest tests
	uv run pytest

ci:  lint fmt ty test  ## Run all CI checks

bench: ## Run benchmark comparing normal vs lazy imports using hyperfine
	@echo "🔥 Benchmarking with Hyperfine"
	@echo "Requires: hyperfine (brew install hyperfine)"
	@echo ""
	@echo "=== CLI --help comparison ==="
	hyperfine --warmup 3 --runs 10 \
		--export-markdown benchmark-results.md \
		--command-name "normal" "uv run breadctl --help" \
		--command-name "lazy" "uv run breadctl-lazy --help"
	@echo ""
	@echo "=== Module import comparison ==="
	hyperfine --warmup 3 --runs 10 \
		--command-name "normal-import" "uv run python -c 'import breadctl.normal'" \
		--command-name "lazy-import" "uv run python -c 'import breadctl.lazy'"
	@echo ""
	@echo "Results saved to benchmark-results.md"

bench-verbose: ## Detailed benchmark with import time tracing
	@echo "=== Import time analysis (normal) ==="
	@uv run python -X importtime -c "import breadctl.normal" 2>&1 | head -20
	@echo ""
	@echo "=== Import time analysis (lazy) ==="
	@uv run python -X importtime -c "import breadctl.lazy" 2>&1 | head -20

clean: ## Remove cache and build artifacts
	rm -rf .pytest_cache .ruff_cache __pycache__ .coverage htmlcov
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name "__pycache__" -exec rm -rf {} +

all: fmt lint ty test ## Run all checks (format, lint, type check, test)
