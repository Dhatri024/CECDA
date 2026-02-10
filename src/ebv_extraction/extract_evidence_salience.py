import os
import re
import pandas as pd
from pathlib import Path

# ----------------------------
# Evidence Keywords
# ----------------------------
DATASET_WORDS = ["dataset", "cifar", "imagenet", "mnist", "benchmark"]
ABLATION_WORDS = ["ablation", "remove", "variant", "component"]
BASELINE_WORDS = ["baseline", "compare", "state-of-the-art", "sota"]
SEED_WORDS = ["seed", "variance", "std", "mean ±"]
FAILURE_WORDS = ["limitation", "failure case", "weakness"]

# ----------------------------
# Evidence Counter
# ----------------------------
def count_matches(text, keywords):
    return sum(text.lower().count(k) for k in keywords)

# ----------------------------
# Salience Weighted EBV
# ----------------------------
def compute_salience_ebv(text):

    lower = text.lower()

    # ----------------------------
    # Split Main vs Appendix
    # ----------------------------
    main_text = lower
    appendix_text = ""

    if "appendix" in lower:
        parts = lower.split("appendix", 1)
        main_text = parts[0]
        appendix_text = parts[1]

    # ----------------------------
    # Evidence Counts
    # ----------------------------
    main_score = (
        count_matches(main_text, DATASET_WORDS)
        + count_matches(main_text, ABLATION_WORDS)
        + count_matches(main_text, BASELINE_WORDS)
        + count_matches(main_text, SEED_WORDS)
        + count_matches(main_text, FAILURE_WORDS)
    )

    appendix_score = (
        count_matches(appendix_text, DATASET_WORDS)
        + count_matches(appendix_text, ABLATION_WORDS)
        + count_matches(appendix_text, BASELINE_WORDS)
        + count_matches(appendix_text, SEED_WORDS)
        + count_matches(appendix_text, FAILURE_WORDS)
    )

    # ----------------------------
    # Salience Weighting
    # ----------------------------
    weighted_score = (1.0 * main_score) + (0.4 * appendix_score)

    # Normalize to [0,1]
    ebv = min(weighted_score / 50, 1.0)

    return round(ebv, 3), main_score, appendix_score

# ----------------------------
# Wrapper Function for Single Paper EBV
# ----------------------------
def extract_ebv_salience(text: str):
    """
    Extract EBV score from ONE paper text.
    Returns: ebv_score (float)
    """

    # Count main evidence keywords
    main_hits = len(re.findall(r"(dataset|experiment|baseline|ablation|results)", text.lower()))

    # Count appendix evidence keywords
    appendix_hits = len(re.findall(r"(appendix|supplementary)", text.lower()))

    # Salience weighting
    ebv_score = (main_hits * 1.0) + (appendix_hits * 0.3)

    # Normalize to [0,1]
    ebv_score = min(1.0, ebv_score / 50)

    return round(ebv_score, 3)



# ----------------------------
# Main Runner
# ----------------------------
def main():
    input_folder = "data/paper_texts"
    output_file = "outputs/ebv_scores_salience.csv"

    results = []

    for file in Path(input_folder).glob("*.txt"):
        paper_id = file.stem
        text = file.read_text(encoding="utf-8")

        ebv, main_score, appendix_score = compute_salience_ebv(text)

        results.append({
            "paper_id": paper_id,
            "ebv_score": ebv,
            "main_evidence": main_score,
            "appendix_evidence": appendix_score
        })

    df = pd.DataFrame(results)
    df.to_csv(output_file, index=False)

    print("\n✅ Salience-Aware EBV Complete!")
    print("Saved to:", output_file)
    print(df.head())


if __name__ == "__main__":
    main()
