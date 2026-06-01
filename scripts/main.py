from extract import extract_data
from transform import transform_data
from load import load_data

def run_etl():
    print("=" * 50)
    print("STARTING MOVIE ETL PIPELINE")
    print("=" * 50)

    # Extract
    df = extract_data()
    print("\nExtract stage completed.")
    print(f"Original Shape: {df.shape}")

    # Transform
    clean_df = transform_data(df)
    print("\nTransform stage completed.")
    print(f"Cleaned Shape: {clean_df.shape}")

    # Save cleaned CSV
    clean_df.to_csv("data/cleaned_box_office_dataset.csv", index=False)
    print("\nCleaned file saved as: data/cleaned_box_office_dataset.csv")

    # Load
    load_data(clean_df)

    print("\nETL Pipeline Completed Successfully!")

if __name__ == "__main__":
    run_etl()