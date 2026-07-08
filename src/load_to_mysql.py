import pandas as pd
import mysql.connector

from config.config import PROCESSED_DATA_PATH
from logger import logger


logger.info("MySQL load started")

try:

    df = pd.read_csv(PROCESSED_DATA_PATH)

    logger.info(f"Records ready for loading: {len(df)}")


    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        database="retail_dw"
    )


    cursor = connection.cursor()

    logger.info("Database connection successful")


    # Remove old records before loading new data
    cursor.execute("TRUNCATE TABLE sales")

    logger.info("Existing sales data cleared")


    insert_query = """
    INSERT INTO sales
    (
        order_id,
        customer_id,
        product,
        category,
        quantity,
        price,
        order_date,
        total_sales
    )
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
    """


    for _, row in df.iterrows():

        cursor.execute(
            insert_query,
            (
                row["order_id"],
                row["customer_id"],
                row["product"],
                row["category"],
                row["quantity"],
                row["price"],
                row["order_date"],
                row["total_sales"]
            )
        )


    connection.commit()


    logger.info(
        f"Successfully loaded {len(df)} records into MySQL"
    )


    print("Data Loaded Into MySQL Successfully")


except Exception as e:

    logger.error(f"MySQL Load Failed: {e}")
    raise


finally:

    if 'connection' in locals() and connection.is_connected():

        cursor.close()
        connection.close()

        logger.info("Database connection closed")
