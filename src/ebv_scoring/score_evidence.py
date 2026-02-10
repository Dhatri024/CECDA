import os
import re
import pandas as pd
from pathlib import Path

# ----------------------------
# Evidence keyword patterns
# ----------------------------
DATASET_WORDS = ["dataset", "benchmark", "cifar", "imagenet", "mnist"]
ABLATION_WORDS = ["ablation", "ablate"]
BASELINE_WORDS = ["baseline", "state-of-the-art", "sota"]
SEED_WORDS = ["seed", "variance", "std", "standard deviation"]
FAILURE_WORDS = ["limitation", "failure case", "we observe that"]

# ----------------------------
# Count occurrences helper
# ----------------------------
def count_matches(text, word_list):
    count = 0
    for w in word_list:
        count += len(re.findall(w, text))
    return count


# ----------------------------
# EBV Computation Function
# ----------------------------
def compute_ebv(text):
    text = text.lower()

    dataset_count = count_matches(text, DATASET_WORDS)
    ablation_count = count_matches(text, ABLATION_WORDS)
    baseline_count = count_matches(text, BASELINE_WORDS)
    seed_count = count_matches(text, SEED_WORDS)
    failure_count = count_matches(text, FAILURE_WORDS)

    # Cap values (avoid ablation spam gaming)
    dataset_score = min(dataset_count, 5) / 5
    ablation_score = min(ablation_count, 3) / 3
    baseline_score = min(baseline_count, 5) / 5
    seed_score = min(seed_count, 2) / 2
    failure_score = min(failure_count, 1) / 1

    # Weighted EBV (more importance to datasets + baselines)
    ebv = (
        0.30 * dataset_score +
        0.25 * baseline_score +
        0.20 * ablation_score +
        0.15 * seed_score +
        0.10 * failure_score
    )

    return round(ebv, 3)


# ----------------------------
# Main Runner
# ----------------------------
def main():
    input_folder = "data/paper_texts"
    output_file = "outputs/ebv_scores.csv"

    all_scores = []

    for file in Path(input_folder).glob("*.txt"):
        paper_id = file.stem
        text = file.read_text(encoding="utf-8")

        ebv_score = compute_ebv(text)

        all_scores.append({
            "paper_id": paper_id,
            "ebv_score": ebv_score
        })

    df = pd.DataFrame(all_scores)
    df.to_csv(output_file, index=False)

    print("\n✅ EBV Scoring Complete!")
    print("Saved to:", output_file)
    print(df.head())


if __name__ == "__main__":
    main()
