import pandas as pd
from extract import extract_data



def transform_data(df):
    df = df.copy()

   
    # 1. CLEAN COLUMN NAMES
    
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")


    # 2. REMOVE DUPLICATES
  
    df = df.drop_duplicates()

    print("\nNull values before cleaning:")
    print(df.isnull().sum())

    # Remove rows with null values
    df = df.dropna()

    print("\nNull values after cleaning:")
    print(df.isnull().sum())

    # 4. CHECK / CONVERT DATA TYPES
    print("\nData types before conversion:")
    print(df.dtypes)

    # Convert year to int
    if "year" in df.columns:
        df["year"] = df["year"].astype(int)

    print("\nData types after conversion:")
    print(df.dtypes)

   
    # 5. REMOVE COMMAS FROM RANK COLUMN
    if "rank" in df.columns:
        df["rank"] = df["rank"].astype(str).str.replace(",", "")
        df["rank"] = df["rank"].astype(int)

    # 6. CONVERT NUMERIC COLUMNS IF NEEDED
    numeric_cols = [
        "worldwide_lifetime_gross",
        "domestic_lifetime_gross",
        "domestic_percentage",
        "foreign_lifetime_gross",
        "foreign_percentage"
    ]

    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # Drop rows again if conversion created nulls
    df = df.dropna()

    # 7. CREATE NEW COLUMNS
    if "year" in df.columns:
        df["movie_age"] = 2026 - df["year"]

    if "worldwide_lifetime_gross" in df.columns:
        df["gross_in_crores"] = df["worldwide_lifetime_gross"] / 10000000

    # 8. FILTER DATA
    # Keep movies released after 2000
    if "year" in df.columns:
        df = df[df["year"] >= 2000]

  
    # 9. SORT DATA
    if "worldwide_lifetime_gross" in df.columns:
        df = df.sort_values(by="worldwide_lifetime_gross", ascending=False)

    # 10. RESET INDEX
    df = df.reset_index(drop=True)

    return df


# TEST RUN
df = extract_data()
clean_df = transform_data(df)

print("\n" + "="*50)
print("ORIGINAL DATA (First 10 rows)")
print("="*50)
print(df.head(10))

print("\n" + "="*50)
print("TRANSFORMED DATA (First 10 rows)")
print("="*50)
print(clean_df.head(10))

print("\n" + "="*50)
print("ORIGINAL COLUMNS")
print("="*50)
print(df.columns)

print("\n" + "="*50)
print("TRANSFORMED COLUMNS")
print("="*50)
print(clean_df.columns)

print("\n" + "="*50)
print("ORIGINAL SHAPE")
print("="*50)
print(df.shape)

print("\n" + "="*50)
print("TRANSFORMED SHAPE")
print("="*50)
print(clean_df.shape)

print("\n" + "="*50)
print("SUMMARY STATISTICS")
print("="*50)
print(clean_df.describe())

# Save transformed file
clean_df.to_csv("data/cleaned_box_office_dataset.csv", index=False)
print("\n Cleaned file saved as: data/cleaned_box_office_dataset.csv")

print(df.info())