import pandas as pd
from rapidfuzz import fuzz

# Load extracted claims
pred = pd.read_csv("outputs/claims/extracted_claims.csv")

# Load gold pilot labels
gold = pd.read_csv("data/annotations/pilot_labels_v2.csv")

# Clean text
def clean(t):
    return str(t).lower().replace("\n", " ").strip()

pred_claims = list(pred["claim_sentence"].apply(clean))
gold_claims = list(gold["claim_text"].apply(clean))

# Fuzzy match threshold
THRESHOLD = 70

true_positive = 0
matched_gold = set()

for g in gold_claims:
    for p in pred_claims:
        score = fuzz.partial_ratio(g, p)
        if score >= THRESHOLD:
            true_positive += 1
            matched_gold.add(g)
            break

false_negative = len(gold_claims) - len(matched_gold)
false_positive = len(pred_claims) - true_positive

precision = true_positive / (true_positive + false_positive + 1e-9)
recall = true_positive / (true_positive + false_negative + 1e-9)

print("\n✅ CLAIM EXTRACTION EVALUATION (FUZZY MATCHING)\n")
print("Gold Claims:", len(gold_claims))
print("Predicted Claims:", len(pred_claims))

print("\nTrue Positives:", true_positive)
print("False Positives:", false_positive)
print("False Negatives:", false_negative)

print("\nPrecision:", round(precision, 3))
print("Recall:", round(recall, 3))
print("\nThreshold Used:", THRESHOLD)
