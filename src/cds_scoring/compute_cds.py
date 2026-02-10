import pandas as pd


# ----------------------------
# Severity Band Function (Scientific Thresholds)
# ----------------------------
def assign_severity(cds):
    """
    Scientific CDS interpretation:

    CDS < -0.2   → Evidence much stronger than claim
    -0.2 to 0.1  → Claim and evidence aligned
    0.1 to 0.3   → Moderate divergence (possible overclaim)
    > 0.3        → High divergence (overclaim risk)
    """
    if cds < -0.2:
        return "Strongly Supported"
    elif -0.2 <= cds < 0.1:
        return "Aligned"
    elif 0.1 <= cds < 0.3:
        return "Moderate Divergence"
    else:
        return "High Divergence (Overclaim Risk)"


def main():
    # ----------------------------
    # Input files
    # ----------------------------
    csv_file = "outputs/csv_scored_claims.csv"
    ebv_file = "outputs/ebv_scores.csv"

    # ----------------------------
    # Output files
    # ----------------------------
    output_file = "outputs/final_claim_scores.csv"
    paper_level_file = "outputs/paper_level_cds.csv"

    # ----------------------------
    # Load CSV-scored claims
    # ----------------------------
    claims_df = pd.read_csv(csv_file)

    # ----------------------------
    # Load EBV per paper
    # ----------------------------
    ebv_df = pd.read_csv(ebv_file)

    # ----------------------------
    # Merge EBV into claim dataframe
    # ----------------------------
    merged = claims_df.merge(ebv_df, on="paper_id", how="left")

    # Fill missing EBV values with 0 (safety)
    merged["ebv_score"] = merged["ebv_score"].fillna(0)

    # ----------------------------
    # Compute CDS = CSV - EBV
    # ----------------------------
    merged["cds_score"] = merged["csv_score"] - merged["ebv_score"]

    # ----------------------------
    # Assign Severity Labels
    # ----------------------------
    merged["severity"] = merged["cds_score"].apply(assign_severity)

    # ----------------------------
    # Save Claim-Level Results
    # ----------------------------
    merged.to_csv(output_file, index=False)

    print("\n✅ CDS Computation Complete!")
    print("Saved Claim-Level Results to:", output_file)

    # ----------------------------
    # Fixed Scientific Threshold Bands
    # ----------------------------
    print("\n📌 Scientific CDS Severity Bands Used:")
    print("Strongly Supported : CDS < -0.2")
    print("Aligned            : -0.2 ≤ CDS < 0.1")
    print("Moderate Divergence: 0.1 ≤ CDS < 0.3")
    print("High Divergence    : CDS ≥ 0.3")

    # ----------------------------
    # Show Top Overclaiming Risk Claims
    # ----------------------------
    print("\n🔥 Top 5 Highest CDS Claims (Overclaim Risk):")
    print(
        merged.sort_values("cds_score", ascending=False)
        .head(5)[
            ["paper_id", "claim_sentence", "csv_score", "ebv_score", "cds_score", "severity"]
        ]
    )

    # ----------------------------
    # Show Strongest Supported Claims
    # ----------------------------
    print("\n🟢 Top 5 Most Supported Claims (Lowest CDS):")
    print(
        merged.sort_values("cds_score", ascending=True)
        .head(5)[
            ["paper_id", "claim_sentence", "csv_score", "ebv_score", "cds_score", "severity"]
        ]
    )

    # ----------------------------
    # Summary Stats
    # ----------------------------
    print("\n📊 CDS Summary Statistics:")
    print(merged["cds_score"].describe())

    # ----------------------------
    # Severity Breakdown
    # ----------------------------
    print("\n📌 Severity Distribution:")
    print(merged["severity"].value_counts())

    # ----------------------------
    # Paper-Level CDS Report (Sprint 11 Ready)
    # ----------------------------
    paper_scores = (
        merged.groupby("paper_id")["cds_score"]
        .max()
        .reset_index()
        .sort_values("cds_score", ascending=False)
    )

    paper_scores.to_csv(paper_level_file, index=False)

    print("\n✅ Paper-Level CDS Report Generated!")
    print("Saved to:", paper_level_file)

    print("\n📌 Top Papers by Worst-Case Divergence:")
    print(paper_scores.head(5))


if __name__ == "__main__":
    main()
