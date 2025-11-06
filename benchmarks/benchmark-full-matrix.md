## Full Matrix: All Variants × bake command

| Command | Mean [ms] | Min [ms] | Max [ms] | Relative |
|:---|---:|---:|---:|---:| 
| `uv run breadctl bake` | 560.4 ± 7.0 | 552.6 | 575.3 | 1.42 ± 0.03 |
| `uv run breadctl-lazy bake` | 500.9 ± 6.6 | 492.0 | 508.6 | 1.27 ± 0.03 |
| `uv run breadctl-click bake` | 509.8 ± 7.6 | 500.5 | 521.1 | 1.29 ± 0.03 |
| `uv run breadctl-click-lazy bake` | 394.1 ± 5.8 | 386.1 | 403.6 | 1.00 |
| `uv run breadctl-cyclopts bake` | 531.0 ± 6.5 | 516.2 | 539.7 | 1.35 ± 0.03 |
| `uv run breadctl-cyclopts-lazy bake` | 426.8 ± 7.2 | 416.2 | 435.4 | 1.08 ± 0.02 |

## Full Matrix: All Variants × deliver command

| Command | Mean [ms] | Min [ms] | Max [ms] | Relative |
|:---|---:|---:|---:|---:|
| `uv run breadctl deliver` | 458.3 ± 7.1 | 439.5 | 462.6 | 1.13 ± 0.03 |
| `uv run breadctl-lazy deliver` | 453.0 ± 2.6 | 447.4 | 457.1 | 1.12 ± 0.02 |
| `uv run breadctl-click deliver` | 408.7 ± 3.1 | 404.0 | 413.7 | 1.01 ± 0.02 |
| `uv run breadctl-click-lazy deliver` | 404.6 ± 7.1 | 393.4 | 416.4 | 1.00 |
| `uv run breadctl-cyclopts deliver` | 422.4 ± 8.1 | 404.2 | 431.5 | 1.04 ± 0.03 |
| `uv run breadctl-cyclopts-lazy deliver` | 425.0 ± 3.9 | 416.8 | 430.4 | 1.05 ± 0.02 |

## Full Matrix: All Variants × inventory command

| Command | Mean [ms] | Min [ms] | Max [ms] | Relative |
|:---|---:|---:|---:|---:|
| `uv run breadctl inventory` | 558.2 ± 8.1 | 544.8 | 569.6 | 1.39 ± 0.02 |
| `uv run breadctl-lazy inventory` | 502.0 ± 8.1 | 491.3 | 515.4 | 1.25 ± 0.02 |
| `uv run breadctl-click inventory` | 510.9 ± 3.8 | 506.6 | 516.9 | 1.27 ± 0.01 |
| `uv run breadctl-click-lazy inventory` | 400.8 ± 3.2 | 396.0 | 405.2 | 1.00 |
| `uv run breadctl-cyclopts inventory` | 530.7 ± 7.3 | 516.8 | 540.7 | 1.32 ± 0.02 |
| `uv run breadctl-cyclopts-lazy inventory` | 428.8 ± 8.2 | 416.9 | 442.6 | 1.07 ± 0.02 |
