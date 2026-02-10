import pandas as pd

v1 = pd.read_csv("data/annotations/pilot_labels_v1.csv")
v2 = pd.read_csv("data/annotations/pilot_labels_v2.csv")

merged = v1.merge(
    v2,
    on=["paper_id", "claim_text"],
    suffixes=("_v1", "_v2")
)

csv_match = (merged["csv_score_v1"] == merged["csv_score_v2"]).mean()
ebv_match = (merged["ebv_score_v1"] == merged["ebv_score_v2"]).mean()

print("\n✅ SELF CONSISTENCY REPORT (Sprint 4)\n")
print(f"Total Claims Compared: {len(merged)}")
print(f"CSV Agreement: {csv_match*100:.2f}%")
print(f"EBV Agreement: {ebv_match*100:.2f}%")
