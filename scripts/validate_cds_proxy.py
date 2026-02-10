import pandas as pd

def main():
    file = "outputs/final_claim_scores_calibrated.csv"
    df = pd.read_csv(file)

    print("\n📌 Sprint 11: BASIC VALIDATION REPORT")

    # Paper-level aggregation
    paper_summary = df.groupby("paper_id").agg({
        "cds_score": ["mean", "max"],
        "ebv_score": "mean",
        "csv_score": "mean"
    })

    paper_summary.columns = ["cds_mean", "cds_max", "ebv_mean", "csv_mean"]
    paper_summary = paper_summary.reset_index()

    # Correlations
    print("\n📊 Correlation Checks:")
    print("CDS vs EBV (should be negative):",
          paper_summary["cds_mean"].corr(paper_summary["ebv_mean"]))

    print("CDS vs CSV (should be positive):",
          paper_summary["cds_mean"].corr(paper_summary["csv_mean"]))

    # Show Top Divergence Papers
    print("\n🔥 Top 3 Papers with Highest Divergence Risk:")
    print(paper_summary.sort_values("cds_max", ascending=False).head(3))

    # Save validation report
    paper_summary.to_csv("outputs/sprint11_validation_report.csv", index=False)

    print("\n✅ Validation Report Saved:")
    print("outputs/sprint11_validation_report.csv")


if __name__ == "__main__":
    main()
