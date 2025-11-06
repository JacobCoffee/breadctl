# breadctl Benchmark Results

Generated: Thu Nov  6 10:59:36 CST 2025

## CLI Framework Comparison (--help command)

| Command | Mean [ms] | Min [ms] | Max [ms] | Relative |
|:---|---:|---:|---:|---:|
| `uv run breadctl --help` | 233.7 ± 14.9 | 216.6 | 262.8 | 1.79 ± 0.12 |
| `uv run breadctl-lazy --help` | 184.1 ± 8.7 | 177.0 | 207.7 | 1.41 ± 0.07 |
| `uv run breadctl-click --help` | 170.0 ± 1.2 | 168.3 | 171.7 | 1.31 ± 0.02 |
| `uv run breadctl-click-lazy --help` | 130.2 ± 2.1 | 128.7 | 135.6 | 1.00 |
| `uv run breadctl-cyclopts --help` | 211.8 ± 7.7 | 205.9 | 227.2 | 1.63 ± 0.06 |
| `uv run breadctl-cyclopts-lazy --help` | 159.0 ± 2.0 | 156.7 | 161.9 | 1.22 ± 0.02 |
## Full matrix with all subcommands

| Command | Mean [ms] | Min [ms] | Max [ms] | Relative |
|:---|---:|---:|---:|---:|
| `uv run breadctl --help` | 215.2 ± 4.1 | 211.1 | 224.0 | 1.31 ± 0.03 |
| `uv run breadctl-lazy --help` | 164.7 ± 2.0 | 163.1 | 168.8 | 1.00 |
| `uv run breadctl bake` | 537.3 ± 7.4 | 528.7 | 552.0 | 3.26 ± 0.06 |
| `uv run breadctl-lazy bake` | 538.5 ± 6.9 | 525.5 | 546.1 | 3.27 ± 0.06 |
| `uv run breadctl deliver` | 433.7 ± 9.0 | 415.7 | 445.8 | 2.63 ± 0.06 |
| `uv run breadctl-lazy deliver` | 432.3 ± 8.0 | 421.7 | 441.3 | 2.63 ± 0.06 |
| `uv run breadctl inventory` | 537.7 ± 14.2 | 518.5 | 561.6 | 3.27 ± 0.09 |
| `uv run breadctl-lazy inventory` | 537.2 ± 5.1 | 529.7 | 543.4 | 3.26 ± 0.05 |

## Using `python -c 'import breadctl.{normal,lazy}'`

| Command | Mean [ms] | Min [ms] | Max [ms] | Relative |
|:---|---:|---:|---:|---:|
| `uv run python -c 'import breadctl_cappa.normal'` | 197.8 ± 3.2 | 195.3 | 205.4 | 1.34 ± 0.02 |
| `uv run python -c 'import breadctl_cappa.lazy'` | 147.3 ± 1.2 | 146.3 | 149.5 | 1.00 |
