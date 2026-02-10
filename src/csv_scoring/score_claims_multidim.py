import pandas as pd

# ----------------------------
# Single Claim Scoring Function
# ----------------------------
def score_claim(sentence: str):
    """
    Scores ONE claim sentence using the multi-dimensional rubric.
    Returns: csv_score, modality, comparative, generality, scope
    """

    s = sentence.lower()

    # ----------------------------
    # Modality (weak vs strong language)
    # ----------------------------
    if "may" in s or "might" in s:
        modality = 0.2
    elif "we show" in s or "we demonstrate" in s:
        modality = 0.7
    elif "outperforms" in s or "state-of-the-art" in s:
        modality = 1.0
    else:
        modality = 0.5

    # ----------------------------
    # Comparative Force
    # ----------------------------
    if "outperform" in s or "better than" in s:
        comparative = 1.0
    elif "improve" in s or "boost" in s:
        comparative = 0.6
    else:
        comparative = 0.3

    # ----------------------------
    # Generality
    # ----------------------------
    if "across tasks" in s or "generalization" in s:
        generality = 1.0
    elif "dataset" in s or "benchmark" in s:
        generality = 0.6
    else:
        generality = 0.4

    # ----------------------------
    # Scope
    # ----------------------------
    if "framework" in s or "system" in s:
        scope = 0.8
    elif "method" in s or "approach" in s:
        scope = 0.6
    else:
        scope = 0.4

    # ----------------------------
    # Final CSV Score (average)
    # ----------------------------
    csv_score = round((modality + comparative + generality + scope) / 4, 3)

    return csv_score, modality, comparative, generality, scope

# ----------------------------
# Dimension Scoring Functions
# ----------------------------

def modality_score(s):
    s = s.lower()
    if any(w in s for w in ["may", "might", "could", "suggest"]):
        return 0.2
    if any(w in s for w in ["we show", "we demonstrate"]):
        return 0.6
    if any(w in s for w in ["we prove", "guarantee", "always"]):
        return 1.0
    return 0.5


def comparative_score(s):
    s = s.lower()
    if any(w in s for w in ["outperforms", "state-of-the-art", "sota", "superior"]):
        return 1.0
    if any(w in s for w in ["improves", "better", "boosts"]):
        return 0.6
    return 0.3


def generality_score(s):
    s = s.lower()
    if any(w in s for w in ["all", "any", "universal", "general"]):
        return 1.0
    if any(w in s for w in ["multiple datasets", "variety", "broad"]):
        return 0.7
    return 0.4


def scope_score(s):
    s = s.lower()
    if any(w in s for w in ["framework", "system", "end-to-end", "pipeline"]):
        return 1.0
    if any(w in s for w in ["module", "component", "mechanism"]):
        return 0.6
    return 0.4


# ----------------------------
# Final CSV Score Aggregation
# ----------------------------

def compute_csv(sentence):
    m = modality_score(sentence)
    c = comparative_score(sentence)
    g = generality_score(sentence)
    sc = scope_score(sentence)

    # Weighted average
    final = (0.3 * m) + (0.3 * c) + (0.2 * g) + (0.2 * sc)

    return round(final, 3), m, c, g, sc


# ----------------------------
# Main Runner
# ----------------------------

def main():
    input_file = "outputs/claims/extracted_claims.csv"
    output_file = "outputs/csv_scored_claims_multidim.csv"

    df = pd.read_csv(input_file)

    results = df["claim_sentence"].apply(compute_csv)

    df["csv_score"] = results.apply(lambda x: x[0])
    df["modality"] = results.apply(lambda x: x[1])
    df["comparative"] = results.apply(lambda x: x[2])
    df["generality"] = results.apply(lambda x: x[3])
    df["scope"] = results.apply(lambda x: x[4])

    df.to_csv(output_file, index=False)

    print("✅ Multi-Dimensional CSV Scoring Complete!")
    print("Saved to:", output_file)


if __name__ == "__main__":
    main()
