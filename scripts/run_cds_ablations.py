import pandas as pd

def main():
    file = "outputs/final_claim_scores_multidim.csv"
    df = pd.read_csv(file)

    print("\n📌 Sprint 9: CDS ABLATION REPORT")

    # Full CDS
    df["cds_full"] = df["csv_score"] - df["ebv_score"]

    # Ablation 1: Remove comparative force
    df["csv_no_comparative"] = (
        df["modality"] + df["generality"] + df["scope"]
    ) / 3
    df["cds_no_comparative"] = df["csv_no_comparative"] - df["ebv_score"]

    # Ablation 2: Remove modality
    df["csv_no_modality"] = (
        df["comparative"] + df["generality"] + df["scope"]
    ) / 3
    df["cds_no_modality"] = df["csv_no_modality"] - df["ebv_score"]

    # Compare correlation
    print("\nCorrelation with Full CDS:")
    print("No Comparative:", df["cds_full"].corr(df["cds_no_comparative"]))
    print("No Modality   :", df["cds_full"].corr(df["cds_no_modality"]))

    # Save ablation outputs
    df.to_csv("outputs/cds_ablation_report.csv", index=False)

    print("\n✅ Ablation report saved:")
    print("outputs/cds_ablation_report.csv")

if __name__ == "__main__":
    main()
