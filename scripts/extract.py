import pandas as pd
def extract_data():
  df=pd.read_csv("data/box_office_dataset.csv")
  return df

print(extract_data())