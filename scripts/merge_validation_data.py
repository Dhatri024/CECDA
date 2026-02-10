import pandas as pd

def main():
    cds_file = "outputs/paper_level_cds.csv"
    metadata_file = "data/metadata/papers_metadata.csv"

    output_file = "outputs/validation_ready.csv"

    # Load CDS per paper
    cds_df = pd.read_csv(cds_file)

    # Load metadata
    meta_df = pd.read_csv(metadata_file)

    # Merge
    merged = cds_df.merge(meta_df, on="paper_id", how="left")

    merged.to_csv(output_file, index=False)

    print("\n✅ Validation Dataset Ready!")
    print("Saved to:", output_file)
    print("\nPreview:")
    print(merged.head())

if __name__ == "__main__":
    main()
