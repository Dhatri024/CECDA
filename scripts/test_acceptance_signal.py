import pandas as pd

def main():
    df = pd.read_csv("outputs/validation_ready.csv")

    # Separate accepted vs rejected
    accepted = df[df["accepted"] == True]["cds_score"]
    rejected = df[df["accepted"] == False]["cds_score"]

    print("\n📌 Acceptance Validation Check")
    print("Accepted Papers Mean CDS:", accepted.mean())

    if len(rejected) > 0:
        print("Rejected Papers Mean CDS:", rejected.mean())
    else:
        print("⚠ No rejected papers in dataset yet (need more papers)")

if __name__ == "__main__":
    main()
