import pandas as pd
import matplotlib.pyplot as plt
import os


def main():
    # ----------------------------
    # Load Dataset Results
    # ----------------------------
    dataset_file = "outputs/final_claim_scores_calibrated.csv"

    # Load User Paper Results
    user_file = "outputs/user_demo/my_paper1_cecda_results.csv"

    df_dataset = pd.read_csv(dataset_file)
    df_user = pd.read_csv(user_file)

    # ----------------------------
    # Extract CDS Scores
    # ----------------------------
    dataset_cds = df_dataset["cds_score"]
    user_cds = df_user["cds_score"]

    # ----------------------------
    # Plot 1: Histogram Comparison
    # ----------------------------
    plt.figure()
    plt.hist(dataset_cds, alpha=0.6, label="NeurIPS/ICLR Dataset")
    plt.hist(user_cds, alpha=0.6, label="User IEEE Paper")

    plt.title("CDS Score Distribution Comparison")
    plt.xlabel("CDS Score")
    plt.ylabel("Number of Claims")
    plt.legend()

    os.makedirs("outputs/plots", exist_ok=True)
    plt.savefig("outputs/plots/cds_distribution.png")

    print("✅ Saved Plot: outputs/plots/cds_distribution.png")

    # ----------------------------
    # Plot 2: Average CDS Comparison Bar Chart
    # ----------------------------
    plt.figure()

    avg_dataset = dataset_cds.mean()
    avg_user = user_cds.mean()

    plt.bar(["Dataset Papers", "User IEEE Paper"], [avg_dataset, avg_user])

    plt.title("Average CDS Comparison")
    plt.ylabel("Mean CDS Score")

    plt.savefig("outputs/plots/avg_cds_comparison.png")

    print("✅ Saved Plot: outputs/plots/avg_cds_comparison.png")

    # ----------------------------
    # Plot 3: Severity Band Counts (Dataset)
    # ----------------------------
    plt.figure()

    band_counts = df_dataset["band"].value_counts()

    plt.bar(band_counts.index, band_counts.values)

    plt.title("Dataset Severity Band Distribution")
    plt.xlabel("Band")
    plt.ylabel("Count")

    plt.savefig("outputs/plots/band_distribution.png")

    print("✅ Saved Plot: outputs/plots/band_distribution.png")


if __name__ == "__main__":
    main()
