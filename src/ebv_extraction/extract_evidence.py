import os
import re
import pandas as pd
from pathlib import Path


# ----------------------------
# Evidence Patterns
# ----------------------------
DATASET_PATTERNS = [
    "dataset", "cifar", "imagenet", "mnist",
    "deepmind lab", "robomimic", "benchmark"
]

ABLATION_PATTERNS = [
    "ablation", "component analysis", "remove"
]

BASELINE_PATTERNS = [
    "baseline", "compared against", "state-of-the-art",
    "sota", "prior methods"
]

SEED_PATTERNS = [
    "random seed", "5 runs", "mean ±", "std", "variance"
]

FAILURE_PATTERNS = [
    "limitation", "failure case", "weakness", "future work"
]


# ----------------------------
# Evidence Counting Function
# ----------------------------
def compute_ebv_score(text):
    text = text.lower()

    dataset_count = sum(1 for p in DATASET_PATTERNS if p in text)
    ablation_count = sum(1 for p in ABLATION_PATTERNS if p in text)
    baseline_count = sum(1 for p in BASELINE_PATTERNS if p in text)
    seed_count = sum(1 for p in SEED_PATTERNS if p in text)
    failure_count = sum(1 for p in FAILURE_PATTERNS if p in text)

    # Weighted EBV formula
    score = (
        0.25 * dataset_count +
        0.20 * ablation_count +
        0.20 * baseline_count +
        0.20 * seed_count +
        0.15 * failure_count
    )

    # Normalize into [0,1]
    score = min(score / 5, 1.0)

    return round(score, 3)


# ----------------------------
# Main Runner
# ----------------------------
def main():
    input_folder = "data/paper_texts"
    output_file = "outputs/ebv_scores.csv"

    os.makedirs("outputs", exist_ok=True)

    records = []

    for file in Path(input_folder).glob("*.txt"):
        paper_id = file.stem
        text = file.read_text(encoding="utf-8")

        ebv = compute_ebv_score(text)

        records.append({
            "paper_id": paper_id,
            "ebv_score": ebv
        })

    df = pd.DataFrame(records)
    df.to_csv(output_file, index=False)

    print("✅ EBV Extraction Complete!")
    print("Saved to:", output_file)
    print(df.head())


if __name__ == "__main__":
    main()
