import pandas as pd
from config.config import PROCESSED_DATA_PATH


df = pd.read_csv(PROCESSED_DATA_PATH)


print("DATA QUALITY REPORT")
print("--------------------")


# Missing values check
print("\nMissing Values:")
print(df.isnull().sum())


# Duplicate check
print("\nDuplicate Records:")
print(df.duplicated().sum())


# Quantity validation
print("\nInvalid Quantity:")
print(df[df["quantity"] <= 0])


# Sales validation
print("\nInvalid Sales:")
print(df[df["total_sales"] <= 0])


print("\nData Quality Check Completed")
