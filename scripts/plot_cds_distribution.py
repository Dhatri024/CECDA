import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("outputs/final_claim_scores.csv")

plt.figure()
plt.hist(df["cds_score"], bins=15)
plt.title("CECDA: CDS Score Distribution")
plt.xlabel("Coverage Divergence Score (CDS)")
plt.ylabel("Number of Claims")
plt.show()
