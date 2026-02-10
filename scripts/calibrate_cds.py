import pandas as pd

def main():
    file = "outputs/final_claim_scores_multidim.csv"
    df = pd.read_csv(file)

    print("\n📌 CDS CALIBRATION REPORT")

    # Percentile thresholds
    p75 = df["cds_score"].quantile(0.75)
    p90 = df["cds_score"].quantile(0.90)

    print("\nThreshold Bands:")
    print("Moderate Divergence (Top 25%):", round(p75, 3))
    print("High Divergence (Top 10%):", round(p90, 3))

    # Assign band labels
    def band(cds):
        if cds >= p90:
            return "High Divergence"
        elif cds >= p75:
            return "Moderate Divergence"
        else:
            return "Aligned/Supported"

    df["band"] = df["cds_score"].apply(band)

    # Save calibrated output
    df.to_csv("outputs/final_claim_scores_calibrated.csv", index=False)

    print("\n✅ Calibrated file saved:")
    print("outputs/final_claim_scores_calibrated.csv")

    print("\n📊 Band Distribution:")
    print(df["band"].value_counts())

if __name__ == "__main__":
    main()
