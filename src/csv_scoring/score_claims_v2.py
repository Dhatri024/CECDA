import pandas as pd

def score_claim(sentence):
    s = sentence.lower()

    score = 0.3  # base

    if "outperforms" in s or "state-of-the-art" in s:
        score += 0.3

    if "we prove" in s or "guarantee" in s:
        score += 0.3

    if "may" in s or "might" in s:
        score -= 0.1

    return min(max(score, 0), 1)


def main():
    input_file = "outputs/claims/extracted_claims.csv"
    output_file = "outputs/csv_scored_claims.csv"

    df = pd.read_csv(input_file)

    df["csv_score"] = df["claim_sentence"].apply(score_claim)

    df.to_csv(output_file, index=False)

    print("✅ CSV Scoring Complete!")
    print("Saved to:", output_file)


if __name__ == "__main__":
    main()
