# breadctl Benchmark Results

Generated: Wed Nov  5 12:40:38 CST 2025

## CLI Framework Comparison (--help command)

| Command                                |    Mean [ms] | Min [ms] | Max [ms] |    Relative |
|:---------------------------------------|-------------:|---------:|---------:|------------:|
| `uv run breadctl --help`               |  245.8 ± 7.0 |    239.5 |    262.7 | 1.61 ± 0.06 |
| `uv run breadctl-lazy --help`          | 202.5 ± 10.5 |    192.4 |    220.7 | 1.32 ± 0.08 |
| `uv run breadctl-click --help`         |  200.8 ± 7.3 |    190.4 |    210.7 | 1.31 ± 0.06 |
| `uv run breadctl-click-lazy --help`    |  152.8 ± 4.1 |    147.5 |    158.7 |        1.00 |
| `uv run breadctl-cyclopts --help`      |  236.9 ± 2.1 |    234.9 |    240.9 | 1.55 ± 0.04 |
| `uv run breadctl-cyclopts-lazy --help` |  182.7 ± 1.3 |    180.5 |    184.6 | 1.20 ± 0.03 |
## Full matrix with all subcommands

| Command                          |   Mean [ms] | Min [ms] | Max [ms] |    Relative |
|:---------------------------------|------------:|---------:|---------:|------------:|
| `uv run breadctl --help`         | 245.1 ± 1.7 |    243.1 |    247.5 | 1.29 ± 0.02 |
| `uv run breadctl-lazy --help`    | 190.7 ± 2.4 |    187.6 |    195.5 |        1.00 |
| `uv run breadctl bake`           | 560.0 ± 5.8 |    550.0 |    570.3 | 2.94 ± 0.05 |
| `uv run breadctl-lazy bake`      | 512.2 ± 7.1 |    500.0 |    523.2 | 2.69 ± 0.05 |
| `uv run breadctl deliver`        | 454.9 ± 7.4 |    442.9 |    464.2 | 2.39 ± 0.05 |
| `uv run breadctl-lazy deliver`   | 452.5 ± 7.2 |    438.3 |    460.0 | 2.37 ± 0.05 |
| `uv run breadctl inventory`      | 558.6 ± 9.0 |    541.6 |    573.1 | 2.93 ± 0.06 |
| `uv run breadctl-lazy inventory` | 512.8 ± 5.8 |    504.0 |    521.1 | 2.69 ± 0.05 |

## Using `python -c 'import breadctl.{normal,lazy}'`

| Command                                           |   Mean [ms] | Min [ms] | Max [ms] |    Relative |
|:--------------------------------------------------|------------:|---------:|---------:|------------:|
| `uv run python -c 'import breadctl_cappa.normal'` | 229.0 ± 4.6 |    222.5 |    236.1 | 1.36 ± 0.03 |
| `uv run python -c 'import breadctl_cappa.lazy'`   | 168.2 ± 1.7 |    166.0 |    171.3 |        1.00 |
