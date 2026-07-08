import pandas as pd
from config.config import RAW_DATA_PATH, PROCESSED_DATA_PATH
from logger import logger


logger.info("Transformation started")

try:

    # Read raw data
    df = pd.read_csv(RAW_DATA_PATH)

    logger.info(f"Input records: {len(df)}")


    # Data quality check
    missing_values = df.isnull().sum().sum()

    logger.info(f"Missing values found: {missing_values}")


    # Transformation
    df["total_sales"] = df["quantity"] * df["price"]


    # Save processed data
    df.to_csv(
        PROCESSED_DATA_PATH,
        index=False
    )


    logger.info(
        f"Transformation completed. Output records: {len(df)}"
    )


    print("Transformation Completed Successfully")
    print(df)


except Exception as e:

    logger.error(f"Transformation failed: {e}")
    raise
