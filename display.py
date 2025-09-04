import json
import os


def display_coverage(title, counts, total_points):
    print("\n" + "="*90)
    print(f"    Quantitative Coverage Analysis ({title})")
    print("="*90 + "\n")

    if total_points > 0:
        print(f"Total points evaluated: {total_points}\n")
        
        for status, count in counts.items():
            percentage = (count / total_points) * 100
            status_display = status.replace("_", " ").title().ljust(20)
            print(f"{status_display}: {count} / {total_points} ({percentage:.2f}%)")
    else:
        print("Could not determine the total number of points for analysis.")

if __name__ == "__main__":
    eval_dir = "data/veritas_eval/gemini-2.5-deep-research"
    with open(os.path.join(eval_dir, "coverage.json"), "r", encoding="utf-8") as f:
        coverages = json.load(f)
    
    coverage_counts = {
        "fully covered": 0,
        "partially covered": 0,
        "not covered": 0,
        "unknown": 0
    }
    total_points = 0
    for stat in coverages:
        print(f"Evaluating coverage for {stat['filename']}...")
        display_coverage(stat['filename'], stat['counts'], stat['total_points'])
        print(stat['evaluation_report'])
        for status, count in stat['counts'].items():
            coverage_counts[status] += count
        total_points += stat['total_points']
    if total_points != sum(coverage_counts.values()):
        print("Warning: Total points do not match sum of individual status counts.")
    display_coverage("deep research", coverage_counts, total_points)
