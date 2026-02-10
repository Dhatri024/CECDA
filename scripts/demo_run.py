import pandas as pd

def main():
    df = pd.read_csv("outputs/final_claim_scores_calibrated.csv")

    print("\n📌 CECDA FINAL DEMO\n")

    print("🔥 Top 5 Overclaim Risk Claims:\n")
    print(df.sort_values("cds_score", ascending=False).head(5))

    print("\n🟢 Top 5 Strongly Supported Claims:\n")
    print(df.sort_values("cds_score", ascending=True).head(5))

if __name__ == "__main__":
    main()
