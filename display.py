import json
import os


def display_coverage(title, counts, total_points):
    content = "="*90 + "\n"
    content += f"Quantitative Coverage Analysis ({title})\n"
    content += "="*90 + "\n"
    
    if total_points > 0:
        content += f"Total points evaluated: {total_points}\n"
        for status, count in counts.items():
            percentage = (count / total_points) * 100
            status_display = status.replace("_", " ").title().ljust(20)
            content += f"{status_display}: {count} / {total_points} ({percentage:.2f}%)\n"
        return content
    else:
        print("Could not determine the total number of points for analysis.")
        return ""

if __name__ == "__main__":
    eval_dir = "data/PubMed/veritas_eval_deepseek_reasoner"
    preds = [
        # "claude-3.7-sonnet",
        # "claude-4-sonnet",
        # "gemini-2.5-deep-research",
        # "gemini-2.5-flash",
        # "gemini-2.5-pro",
        "gpt-5",
        # "gpt-5-mini"
    ]

    with open(os.path.join(eval_dir, "research_coverage.txt"), "a", encoding="utf-8") as f_cov:
        for pred in preds:
            with open(os.path.join(f"{eval_dir}/{pred}", "coverage.json"), "r", encoding="utf-8") as f:
                coverages = json.load(f)
            coverage_counts = {
                "fully covered": 0,
                "partially covered": 0,
                "not covered": 0,
            }
            total_points = 0
            costs = []
            for stat in coverages:
                print(f"Evaluating coverage for {stat['filename']}...")
                print(display_coverage(stat['filename'], stat['counts'], stat['total_points']))
                for status, count in stat['counts'].items():
                    if status == "unknown" and count == 0:
                        continue
                    coverage_counts[status] += count
                total_points += stat['total_points']
                if "total_cost" in stat.get("token_usage", {}):
                    costs.append(stat["token_usage"]["total_cost"])
            if total_points != sum(coverage_counts.values()):
                print("Warning: Total points do not match sum of individual status counts.")
            coverage_content = display_coverage(f"deep research agent powered by {pred}", coverage_counts, total_points)
            print(coverage_content)
            f_cov.write(f"\n\n{coverage_content}\n")
            if len(costs) > 0:
                avg_cost = sum(costs) / len(costs)
                cost_content = f"Average cost per instance: ${avg_cost:.4f}\n"
                print(cost_content)
                f_cov.write(cost_content)
