import pandas as pd

def main():
    df = pd.read_csv("outputs/validation_ready.csv")

    print("\n📌 BASIC VALIDATION REPORT")

    # Overall CDS stats
    print("\nOverall CDS Distribution:")
    print(df["cds_score"].describe())

    # Worst papers
    print("\n🔥 Top 5 Papers with Highest Divergence:")
    print(df.sort_values("cds_score", ascending=False).head(5))

    # Best supported papers
    print("\n🟢 Top 5 Papers with Lowest Divergence:")
    print(df.sort_values("cds_score", ascending=True).head(5))

if __name__ == "__main__":
    main()
