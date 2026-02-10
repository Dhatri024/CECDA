import pandas as pd

INPUT = "outputs/claims/extracted_claims.csv"
OUTPUT = "data/annotations/pilot_gold.csv"

df = pd.read_csv(INPUT)

# Take top 3 claims per paper
sample = df.groupby("paper_id").head(3)

sample["csv_label"] = ""
sample["ebv_label"] = ""
sample["annotator"] = "Dhatri"

sample.to_csv(OUTPUT, index=False)

print("✅ Annotation template created:", OUTPUT)
print("Fill csv_label and ebv_label manually.")
