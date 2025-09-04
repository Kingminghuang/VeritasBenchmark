# print(str.replace("\n", "\\n").replace("\"", "\\\""))
# print(str)

import json

with open("data/veritas_eval/claude-3.7-sonnet/research_plan.txt", "a", encoding="utf-8") as f1:
    with open("data/veritas_eval/claude-3.7-sonnet/coverage.json", "r", encoding="utf-8") as f2:
        data = json.load(f2)
        for item in data:
            if "unknown" in item["counts"] and item["counts"]["unknown"] > 0:
                f1.write(f"\n\n\n\n{item['filename']}:")
                f1.write(f"\n{item['evaluation_report']}")