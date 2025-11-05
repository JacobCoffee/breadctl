# ALL ABOUT THE BRED

## Anthem

```markdown
my name is Cow,
and wen its nite,
or wen the moon
is shiyning brite,
and all the men
haf gon to bed –
i stay up late.
i lik the bred.
```
 - [that guy](https://yeahwrite.me/writing-help-bredlik/)

serious section begins now...

---

# breadctl - PEP 810 Lazy Imports Demo

A demonstration CLI tool showcasing [PEP 810 (Explicit Lazy Imports)](https://peps.python.org/pep-0810/) for 
conference talks and educational purposes.

### [Talk Notes](CONFERENCE.md) 

## What is PEP 810?

PEP 810 introduces explicit lazy imports to Python, allowing modules to be imported only when first accessed 
rather than at import time. This can dramatically improve:

- **Startup time**: ?% faster in some real workloads
- **Memory usage**: %% reduction by keeping unused modules unloaded
- **Developer experience**: "not bad" - most developers

## Project Structure

```
breadctl/
├── src/breadctl/
│   ├── __init__.py
│   ├── normal.py      # Traditional imports (baseline)
│   ├── lazy.py        # CLI but using PEP 810  lazy imports, oooh fancy!
│   ├── bake.py        # Heavy module (pandas, matplotlib)
│   ├── deliver.py     # HTTP module (httpx)
│   └── inventory.py   # Database module (sqlite3)
├── tests/
└── Makefile           # Development tasks & benchmarking
```

## Prerequisites

### 1. Python 3.14 with PEP 810 Support

⚠️ **PEP 810 was recently accepted and is not in any released Python yet.**

You'll need to build CPython from source with the specific implementation of PEP 810.
See [Building CPython from Source][building-cpython] for more informaiton

### 2. Hyperfine (for benchmarking)

See [install instructions on GitHub](https://github.com/sharkdp/hyperfine#installation)

### 3. uv Package Manager

See [Astral.sh instructions](https://docs.astral.sh/uv/getting-started/installation/)

## Installation

```bash
# Clone the repo
git clone https://github.com/JacobCoffee/breadctl.git
cd breadctl

# Install dependencies with uv (using your PEP 810 Python)
make install
```

## Usage

### Normal Version (Baseline)

```bash
uv run breadctl --help
uv run breadctl bake
uv run breadctl deliver
uv run breadctl inventory
```

### Lazy Imports Version (PEP 810)

```bash
uv run breadctl-lazy --help
uv run breadctl-lazy bake
uv run breadctl-lazy deliver
uv run breadctl-lazy inventory
```

## Benchmarking

### Quick Benchmark

```bash
make bench
```

This uses Hyperfine to compare:
- CLI `--help` startup time
- Module import time

Results are saved to `benchmark-results.md`.

### Detailed Import Analysis

```bash
make bench-verbose
```

Shows the import tree and timing for each module.

### Example Output

```
todo
```

## Development

### Run All Checks

```bash
make ci
```

This runs:
- `make fmt` - Format with ruff
- `make lint` - Lint with ruff
- `make ty` - Type check with ty
- `make test` - Run pytest

### Individual Tools

```bash
make lint          # Run linter
make fmt           # Format code
make ty            # Type checking with ty
make test          # Run tests
make bench         # Benchmark with hyperfine
make clean         # Clean build artifacts
```

## Resources

- [PEP 810 - Explicit Lazy Imports](https://peps.python.org/pep-0810/)
- [Python Import System](https://docs.python.org/3/reference/import.html)
- [Building CPython][building-cpython]
- [Hyperfine Benchmarking](https://github.com/sharkdp/hyperfine)

[building-cpython]: https://docs.python.org/3/reference/import.html