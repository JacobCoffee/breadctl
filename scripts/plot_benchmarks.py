"""
Generate visualization charts from benchmark results.

This script parses benchmark-results.md and creates multiple charts:
1. Side-by-side bar chart comparing normal vs lazy
2. Speedup percentage chart
3. Combined chart with error bars
4. Import benchmark comparison
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def parse_benchmark_table(content: str, section_marker: str) -> dict[str, dict]:
    """
    Parse a markdown table from benchmark results.

    Args:
        content: Full markdown content
        section_marker: Section header to find (e.g., "## Full matrix")

    Returns:
        Dictionary mapping command names to their metrics

    """
    # Find the section
    section_start = content.find(section_marker)
    if section_start == -1:
        raise ValueError(f"Section '{section_marker}' not found")

    # Find the table (starts after the header line)
    table_start = content.find("|", section_start)
    next_section = content.find("\n## ", table_start)
    if next_section == -1:
        next_section = len(content)

    table_content = content[table_start:next_section]
    lines = [line.strip() for line in table_content.split("\n") if line.strip().startswith("|")]

    # Skip header and separator lines
    data_lines = [line for line in lines[2:] if not line.startswith("|:")]

    results = {}
    for line in data_lines:
        parts = [p.strip() for p in line.split("|")[1:-1]]  # Remove empty first/last
        if len(parts) < 5:
            continue

        command = parts[0].strip("`")
        mean_str = parts[1].strip()
        min_val = float(parts[2].strip())
        max_val = float(parts[3].strip())

        # Parse mean ± std
        if "±" in mean_str:
            mean, std = mean_str.split("±")
            mean = float(mean.strip())
            std = float(std.strip())
        else:
            mean = float(mean_str)
            std = 0.0

        results[command] = {
            "mean": mean,
            "std": std,
            "min": min_val,
            "max": max_val,
        }

    return results


def create_comparison_chart(subcommand_data: dict, output_path: Path) -> None:
    """Create side-by-side bar chart comparing normal vs lazy."""
    # Extract commands (remove 'uv run breadctl' prefix for cleaner labels)
    commands = ["--help", "bake", "deliver", "inventory"]
    normal_times = []
    lazy_times = []
    normal_errors = []
    lazy_errors = []

    for cmd in commands:
        normal_key = f"uv run breadctl {cmd}"
        lazy_key = f"uv run breadctl-lazy {cmd}"

        normal_times.append(subcommand_data[normal_key]["mean"])
        lazy_times.append(subcommand_data[lazy_key]["mean"])
        normal_errors.append(subcommand_data[normal_key]["std"])
        lazy_errors.append(subcommand_data[lazy_key]["std"])

    x = np.arange(len(commands))
    width = 0.35

    fig, ax = plt.subplots(figsize=(12, 6))
    bars1 = ax.bar(x - width/2, normal_times, width, label="Normal (eager imports)",
                   color="#ef4444", alpha=0.8, yerr=normal_errors, capsize=5)
    bars2 = ax.bar(x + width/2, lazy_times, width, label="Lazy imports (PEP 810)",
                   color="#22c55e", alpha=0.8, yerr=lazy_errors, capsize=5)

    ax.set_xlabel("Command", fontsize=12, fontweight="bold")
    ax.set_ylabel("Execution Time (ms)", fontsize=12, fontweight="bold")
    ax.set_title("CLI Performance: Normal vs Lazy Imports", fontsize=14, fontweight="bold")
    ax.set_xticks(x)
    ax.set_xticklabels(commands)
    ax.legend(fontsize=11)
    ax.grid(axis="y", alpha=0.3)

    # Add value labels on bars
    for bars in [bars1, bars2]:
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f"{height:.1f}ms",
                   ha="center", va="bottom", fontsize=9)

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    print(f"✓ Saved comparison chart to {output_path}")


def create_speedup_chart(subcommand_data: dict, output_path: Path) -> None:
    """Create bar chart showing percentage speedup."""
    commands = ["--help", "bake", "deliver", "inventory"]
    speedups = []
    time_saved = []

    for cmd in commands:
        normal_key = f"uv run breadctl {cmd}"
        lazy_key = f"uv run breadctl-lazy {cmd}"

        normal_time = subcommand_data[normal_key]["mean"]
        lazy_time = subcommand_data[lazy_key]["mean"]

        speedup_pct = ((normal_time - lazy_time) / normal_time) * 100
        speedups.append(speedup_pct)
        time_saved.append(normal_time - lazy_time)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    # Speedup percentage chart
    bars1 = ax1.bar(commands, speedups, color="#3b82f6", alpha=0.8)
    ax1.set_xlabel("Command", fontsize=12, fontweight="bold")
    ax1.set_ylabel("Speedup (%)", fontsize=12, fontweight="bold")
    ax1.set_title("Lazy Import Performance Improvement", fontsize=13, fontweight="bold")
    ax1.grid(axis="y", alpha=0.3)
    ax1.axhline(y=0, color="black", linestyle="-", linewidth=0.8)

    for bar in bars1:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height,
                f"{height:.1f}%",
                ha="center", va="bottom", fontsize=10, fontweight="bold")

    # Time saved chart
    bars2 = ax2.bar(commands, time_saved, color="#8b5cf6", alpha=0.8)
    ax2.set_xlabel("Command", fontsize=12, fontweight="bold")
    ax2.set_ylabel("Time Saved (ms)", fontsize=12, fontweight="bold")
    ax2.set_title("Absolute Time Savings", fontsize=13, fontweight="bold")
    ax2.grid(axis="y", alpha=0.3)

    for bar in bars2:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height,
                f"{height:.1f}ms",
                ha="center", va="bottom", fontsize=10, fontweight="bold")

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    print(f"✓ Saved speedup chart to {output_path}")


def create_import_comparison_chart(import_data: dict, output_path: Path) -> None:
    """Create chart comparing pure import times."""
    commands = [
        "uv run python -c 'import breadctl_cappa.normal'",
        "uv run python -c 'import breadctl_cappa.lazy'"
    ]
    labels = ["Normal", "Lazy"]
    times = [import_data[cmd]["mean"] for cmd in commands]
    errors = [import_data[cmd]["std"] for cmd in commands]
    colors = ["#ef4444", "#22c55e"]

    fig, ax = plt.subplots(figsize=(8, 6))
    bars = ax.bar(labels, times, color=colors, alpha=0.8, yerr=errors, capsize=8)

    ax.set_ylabel("Import Time (ms)", fontsize=12, fontweight="bold")
    ax.set_title("Pure Import Performance Comparison", fontsize=14, fontweight="bold")
    ax.grid(axis="y", alpha=0.3)

    # Add value labels
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
               f"{height:.1f}ms",
               ha="center", va="bottom", fontsize=11, fontweight="bold")

    # Add speedup annotation
    normal_time = times[0]
    lazy_time = times[1]
    speedup = ((normal_time - lazy_time) / normal_time) * 100
    time_saved = normal_time - lazy_time

    ax.text(0.5, max(times) * 0.7,
           f"Speedup: {speedup:.1f}%\n({time_saved:.1f}ms faster)",
           ha="center", va="center",
           bbox=dict(boxstyle="round,pad=0.5", facecolor="yellow", alpha=0.3),
           fontsize=12, fontweight="bold")

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    print(f"✓ Saved import comparison chart to {output_path}")


def create_combined_chart(subcommand_data: dict, import_data: dict, output_path: Path) -> None:
    """Create comprehensive chart with all metrics."""
    fig = plt.figure(figsize=(16, 10))
    gs = fig.add_gridspec(2, 2, hspace=0.3, wspace=0.3)

    # Top left: CLI comparison
    ax1 = fig.add_subplot(gs[0, :])
    commands = ["--help", "bake", "deliver", "inventory"]
    normal_times = []
    lazy_times = []

    for cmd in commands:
        normal_key = f"uv run breadctl {cmd}"
        lazy_key = f"uv run breadctl-lazy {cmd}"
        normal_times.append(subcommand_data[normal_key]["mean"])
        lazy_times.append(subcommand_data[lazy_key]["mean"])

    x = np.arange(len(commands))
    width = 0.35
    ax1.bar(x - width/2, normal_times, width, label="Normal", color="#ef4444", alpha=0.8)
    ax1.bar(x + width/2, lazy_times, width, label="Lazy", color="#22c55e", alpha=0.8)
    ax1.set_xlabel("Command", fontweight="bold")
    ax1.set_ylabel("Time (ms)", fontweight="bold")
    ax1.set_title("CLI Command Performance", fontsize=13, fontweight="bold")
    ax1.set_xticks(x)
    ax1.set_xticklabels(commands)
    ax1.legend()
    ax1.grid(axis="y", alpha=0.3)

    # Bottom left: Import comparison
    ax2 = fig.add_subplot(gs[1, 0])
    import_labels = ["Normal", "Lazy"]
    import_times = [
        import_data["uv run python -c 'import breadctl_cappa.normal'"]["mean"],
        import_data["uv run python -c 'import breadctl_cappa.lazy'"]["mean"]
    ]
    ax2.bar(import_labels, import_times, color=["#ef4444", "#22c55e"], alpha=0.8)
    ax2.set_ylabel("Time (ms)", fontweight="bold")
    ax2.set_title("Pure Import Time", fontsize=13, fontweight="bold")
    ax2.grid(axis="y", alpha=0.3)

    # Bottom right: Speedup percentages
    ax3 = fig.add_subplot(gs[1, 1])
    speedups = []
    for cmd in commands:
        normal = subcommand_data[f"uv run breadctl {cmd}"]["mean"]
        lazy = subcommand_data[f"uv run breadctl-lazy {cmd}"]["mean"]
        speedups.append(((normal - lazy) / normal) * 100)

    ax3.bar(commands, speedups, color="#3b82f6", alpha=0.8)
    ax3.set_ylabel("Improvement (%)", fontweight="bold")
    ax3.set_title("Lazy Import Speedup", fontsize=13, fontweight="bold")
    ax3.grid(axis="y", alpha=0.3)
    ax3.axhline(y=0, color="black", linestyle="-", linewidth=0.8)

    fig.suptitle("breadctl: Lazy Imports Performance Analysis (PEP 810)",
                fontsize=16, fontweight="bold", y=0.995)

    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    print(f"✓ Saved combined chart to {output_path}")


def create_framework_comparison_chart(full_matrix_data: dict, command: str, output_path: Path) -> None:
    """Create chart comparing all frameworks for a specific command."""
    frameworks = ["cappa", "click", "cyclopts"]
    normal_times = []
    lazy_times = []
    normal_errors = []
    lazy_errors = []

    for fw in frameworks:
        normal_key = f"uv run breadctl-{fw} {command}" if fw != "cappa" else f"uv run breadctl {command}"
        lazy_key = f"uv run breadctl-{fw}-lazy {command}" if fw != "cappa" else f"uv run breadctl-lazy {command}"

        normal_times.append(full_matrix_data[normal_key]["mean"])
        lazy_times.append(full_matrix_data[lazy_key]["mean"])
        normal_errors.append(full_matrix_data[normal_key]["std"])
        lazy_errors.append(full_matrix_data[lazy_key]["std"])

    x = np.arange(len(frameworks))
    width = 0.35

    fig, ax = plt.subplots(figsize=(10, 6))
    bars1 = ax.bar(x - width/2, normal_times, width, label="Normal (eager imports)",
                   color="#ef4444", alpha=0.8, yerr=normal_errors, capsize=5)
    bars2 = ax.bar(x + width/2, lazy_times, width, label="Lazy imports",
                   color="#22c55e", alpha=0.8, yerr=lazy_errors, capsize=5)

    ax.set_xlabel("CLI Framework", fontsize=12, fontweight="bold")
    ax.set_ylabel("Execution Time (ms)", fontsize=12, fontweight="bold")
    ax.set_title(f"Framework Comparison: {command} command", fontsize=14, fontweight="bold")
    ax.set_xticks(x)
    ax.set_xticklabels([f.capitalize() for f in frameworks])
    ax.legend(fontsize=11)
    ax.grid(axis="y", alpha=0.3)

    # Add value labels
    for bars in [bars1, bars2]:
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f"{height:.1f}ms",
                   ha="center", va="bottom", fontsize=9)

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    print(f"✓ Saved framework comparison for {command} to {output_path}")


def create_all_frameworks_combined_chart(full_matrix_data: dict, output_path: Path) -> None:
    """Create comprehensive chart showing all frameworks and all commands."""
    commands = ["bake", "deliver", "inventory"]
    frameworks = ["cappa", "click", "cyclopts"]

    fig, axes = plt.subplots(1, 3, figsize=(18, 6))

    for idx, cmd in enumerate(commands):
        ax = axes[idx]

        normal_times = []
        lazy_times = []

        for fw in frameworks:
            normal_key = f"uv run breadctl-{fw} {cmd}" if fw != "cappa" else f"uv run breadctl {cmd}"
            lazy_key = f"uv run breadctl-{fw}-lazy {cmd}" if fw != "cappa" else f"uv run breadctl-lazy {cmd}"

            normal_times.append(full_matrix_data[normal_key]["mean"])
            lazy_times.append(full_matrix_data[lazy_key]["mean"])

        x = np.arange(len(frameworks))
        width = 0.35

        ax.bar(x - width/2, normal_times, width, label="Normal", color="#ef4444", alpha=0.8)
        ax.bar(x + width/2, lazy_times, width, label="Lazy", color="#22c55e", alpha=0.8)

        ax.set_xlabel("Framework", fontweight="bold")
        ax.set_ylabel("Time (ms)", fontweight="bold")
        ax.set_title(f"{cmd.capitalize()}", fontsize=13, fontweight="bold")
        ax.set_xticks(x)
        ax.set_xticklabels([f.capitalize() for f in frameworks])
        if idx == 0:
            ax.legend()
        ax.grid(axis="y", alpha=0.3)

    fig.suptitle("Framework Performance Comparison: All Commands",
                fontsize=16, fontweight="bold", y=1.02)

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    print(f"✓ Saved combined framework comparison to {output_path}")


def create_framework_speedup_chart(full_matrix_data: dict, output_path: Path) -> None:
    """Create chart showing lazy speedup for each framework."""
    commands = ["bake", "deliver", "inventory"]
    frameworks = ["cappa", "click", "cyclopts"]

    fig, ax = plt.subplots(figsize=(12, 6))

    x = np.arange(len(commands))
    width = 0.25

    for i, fw in enumerate(frameworks):
        speedups = []
        for cmd in commands:
            normal_key = f"uv run breadctl-{fw} {cmd}" if fw != "cappa" else f"uv run breadctl {cmd}"
            lazy_key = f"uv run breadctl-{fw}-lazy {cmd}" if fw != "cappa" else f"uv run breadctl-lazy {cmd}"

            normal_time = full_matrix_data[normal_key]["mean"]
            lazy_time = full_matrix_data[lazy_key]["mean"]
            speedup_pct = ((normal_time - lazy_time) / normal_time) * 100
            speedups.append(speedup_pct)

        offset = (i - 1) * width
        colors = ["#3b82f6", "#8b5cf6", "#f59e0b"]
        ax.bar(x + offset, speedups, width, label=fw.capitalize(),
               color=colors[i], alpha=0.8)

    ax.set_xlabel("Command", fontsize=12, fontweight="bold")
    ax.set_ylabel("Speedup (%)", fontsize=12, fontweight="bold")
    ax.set_title("Lazy Import Performance Improvement by Framework", fontsize=14, fontweight="bold")
    ax.set_xticks(x)
    ax.set_xticklabels([cmd.capitalize() for cmd in commands])
    ax.legend(fontsize=11)
    ax.grid(axis="y", alpha=0.3)
    ax.axhline(y=0, color="black", linestyle="-", linewidth=0.8)

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    print(f"✓ Saved framework speedup comparison to {output_path}")


def main() -> None:
    """Main entry point."""
    benchmark_file = Path("benchmarks/benchmark-results.md")
    full_matrix_file = Path("benchmarks/benchmark-full-matrix.md")
    output_dir = Path("benchmarks")
    output_dir.mkdir(exist_ok=True, parents=True)

    # Part 1: Cappa detailed charts (existing functionality)
    if benchmark_file.exists():
        print("📊 Part 1: Parsing cappa benchmark results...")
        content = benchmark_file.read_text()

        try:
            subcommand_data = parse_benchmark_table(content, "## Full matrix with all subcommands")
            import_data = parse_benchmark_table(content, "## Using `python -c 'import breadctl.{normal,lazy}'`")

            print(f"   Found {len(subcommand_data)} subcommand benchmarks")
            print(f"   Found {len(import_data)} import benchmarks")

            print("\n🎨 Generating cappa charts...")
            create_comparison_chart(subcommand_data, output_dir / "comparison.png")
            create_speedup_chart(subcommand_data, output_dir / "speedup.png")
            create_import_comparison_chart(import_data, output_dir / "import-comparison.png")
            create_combined_chart(subcommand_data, import_data, output_dir / "combined.png")

            print("\n✅ Cappa charts generated:")
            print("  - comparison.png        (cappa normal vs lazy)")
            print("  - speedup.png          (cappa speedup metrics)")
            print("  - import-comparison.png (cappa import times)")
            print("  - combined.png         (cappa comprehensive overview)")
        except ValueError as e:
            print(f"⚠️  Could not parse cappa results: {e}")
            print("   Run 'make bench' to generate complete results.")
    else:
        print(f"⚠️  {benchmark_file} not found. Skipping cappa charts.")
        print("   Run 'make bench' to generate cappa benchmark data.")

    # Part 2: Full framework comparison charts (new functionality)
    if full_matrix_file.exists():
        print("\n📊 Part 2: Parsing full framework matrix...")
        content = full_matrix_file.read_text()

        try:
            # Parse each command section
            bake_data = parse_benchmark_table(content, "## Full Matrix: All Variants × bake command")
            deliver_data = parse_benchmark_table(content, "## Full Matrix: All Variants × deliver command")
            inventory_data = parse_benchmark_table(content, "## Full Matrix: All Variants × inventory command")

            # Combine into single dict
            full_matrix_data = {**bake_data, **deliver_data, **inventory_data}

            print(f"   Found {len(full_matrix_data)} framework benchmarks")

            print("\n🎨 Generating framework comparison charts...")

            # Individual command comparisons
            create_framework_comparison_chart(full_matrix_data, "bake",
                                             output_dir / "framework-bake.png")
            create_framework_comparison_chart(full_matrix_data, "deliver",
                                             output_dir / "framework-deliver.png")
            create_framework_comparison_chart(full_matrix_data, "inventory",
                                             output_dir / "framework-inventory.png")

            # Combined framework charts
            create_all_frameworks_combined_chart(full_matrix_data,
                                                output_dir / "framework-all-commands.png")
            create_framework_speedup_chart(full_matrix_data,
                                          output_dir / "framework-speedup.png")

            print("\n✅ Framework comparison charts generated:")
            print("  - framework-bake.png         (all frameworks: bake)")
            print("  - framework-deliver.png      (all frameworks: deliver)")
            print("  - framework-inventory.png    (all frameworks: inventory)")
            print("  - framework-all-commands.png (all frameworks: all commands)")
            print("  - framework-speedup.png      (lazy speedup by framework)")
        except ValueError as e:
            print(f"⚠️  Could not parse full matrix: {e}")
            print("   Run 'make bench-full' to generate framework comparison data.")
    else:
        print(f"\n⚠️  {full_matrix_file} not found. Skipping framework comparison charts.")
        print("   Run 'make bench-full' to generate framework comparison data.")

    print(f"\n🎉 All available charts saved to {output_dir}/")


if __name__ == "__main__":
    main()
