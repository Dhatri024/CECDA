import pandas as pd

def main():
    csv_file = "outputs/csv_scored_claims_multidim.csv"
    ebv_file = "outputs/ebv_scores.csv"
    output_file = "outputs/final_claim_scores_multidim.csv"

    claims = pd.read_csv(csv_file)
    ebv = pd.read_csv(ebv_file)

    merged = claims.merge(ebv, on="paper_id", how="left")
    merged["cds_score"] = merged["csv_score"] - merged["ebv_score"]

    merged.to_csv(output_file, index=False)

    print("✅ Final CDS Computed!")
    print("Saved to:", output_file)

    print("\n🔥 Top Overclaim Risk Claims:")
    print(merged.sort_values("cds_score", ascending=False).head(5))

if __name__ == "__main__":
    main()
