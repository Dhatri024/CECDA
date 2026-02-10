import pandas as pd

df = pd.read_csv("outputs/final_claim_scores.csv")

p75 = df["cds_score"].quantile(0.75)
p90 = df["cds_score"].quantile(0.90)

print("\n📌 CDS Calibration Thresholds:")
print("Moderate Divergence (Top 25%):", round(p75, 3))
print("High Divergence (Top 10%):", round(p90, 3))
