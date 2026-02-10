import pandas as pd

# Keyword-based scoring rubrics
MODALITY = {
    "may": 0.2,
    "can": 0.4,
    "suggest": 0.5,
    "demonstrate": 0.7,
    "show": 0.7,
    "prove": 0.9,
    "guarantee": 1.0
}

COMPARATIVE = {
    "improve": 0.4,
    "outperform": 0.8,
    "state-of-the-art": 1.0,
    "sota": 1.0,
    "superior": 0.8
}

GENERALITY = {
    "on": 0.3,
    "across": 0.7,
    "multiple": 0.6,
    "universal": 1.0,
    "all": 0.9
}

def score_dimension(text, rubric):
    text = text.lower()
    for key, val in rubric.items():
        if key in text:
            return val
    return 0.3  # default baseline


def score_claim(text):
    m = score_dimension(text, MODALITY)
    c = score_dimension(text, COMPARATIVE)
    g = score_dimension(text, GENERALITY)

    csv_score = (m + c + g) / 3
    return csv_score


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
