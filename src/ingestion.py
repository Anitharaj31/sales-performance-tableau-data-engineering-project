import pandas as pd
from config.config import RAW_DATA_PATH
from logger import logger


logger.info("Data ingestion started")


try:
    df = pd.read_csv(RAW_DATA_PATH)

    logger.info(f"Records loaded: {len(df)}")

    print("Sales Data Loaded Successfully")
    print("--------------------------------")
    print(df.head())


except Exception as e:
    logger.error(f"Ingestion failed: {e}")
    raise
