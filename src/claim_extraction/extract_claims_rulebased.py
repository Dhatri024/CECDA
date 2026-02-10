import os
import re
import pandas as pd
from pathlib import Path

# ----------------------------
# Claim Keywords (Universal)
# ----------------------------
CLAIM_KEYWORDS = [
    "propose", "present", "introduce", "develop",
    "demonstrate", "show", "achieve", "outperform",
    "improve", "results", "significantly", "framework",
    "method", "approach", "model", "algorithm",
    "experimental", "evaluation", "performance"
]

# ----------------------------
# Sentence Cleaning
# ----------------------------
def clean_text(text):
    text = text.replace("\n", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()

# ----------------------------
# Sentence Split
# ----------------------------
def split_sentences(text):
    return re.split(r"(?<=[.!?])\s+", text)

# ----------------------------
# Claim Scoring Function
# ----------------------------
def claim_score(sentence):
    score = 0
    lower = sentence.lower()

    for kw in CLAIM_KEYWORDS:
        if kw in lower:
            score += 1

    # bonus if sentence contains numbers (evidence)
    if re.search(r"\d", sentence):
        score += 1

    return score

# ----------------------------
# Extract Claims (Universal)
# ----------------------------
def extract_claim_sentences(text, top_k=10):

    text = clean_text(text)
    sentences = split_sentences(text)

    scored = []

    for sent in sentences:
        sent = sent.strip()

        if len(sent.split()) < 8:
            continue

        if len(sent) > 300:
            continue

        s = claim_score(sent)

        if s >= 2:  # minimum claim relevance
            scored.append((sent, s))

    # Sort by score
    scored = sorted(scored, key=lambda x: x[1], reverse=True)

    # Return top K best claim-like sentences
    return [x[0] for x in scored[:top_k]]

# ----------------------------
# Main Runner
# ----------------------------
def main():
    input_folder = "data/paper_texts"
    output_file = "outputs/claims/extracted_claims.csv"

    os.makedirs("outputs/claims", exist_ok=True)

    all_claims = []

    for file in Path(input_folder).glob("*.txt"):
        paper_id = file.stem
        text = file.read_text(encoding="utf-8", errors="ignore")

        claims = extract_claim_sentences(text)

        for c in claims:
            all_claims.append({
                "paper_id": paper_id,
                "claim_sentence": c
            })

    df = pd.DataFrame(all_claims)
    df.to_csv(output_file, index=False)

    print("\n✅ Universal Claim Extraction Complete!")
    print("Saved to:", output_file)
    print("Total Claims Extracted:", len(df))

if __name__ == "__main__":
    main()
