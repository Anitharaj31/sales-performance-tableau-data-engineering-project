import pandas as pd
import mysql.connector


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    database="retail_dw"
)


queries = {
    "sales_summary":"SELECT * FROM sales_summary",
    "customer_sales":"SELECT * FROM customer_sales",
    "product_performance":"SELECT * FROM product_performance"
}


for name, query in queries.items():

    df = pd.read_sql(query, connection)

    df.to_csv(
        f"reports/{name}.csv",
        index=False
    )

    print(name,"export completed")


connection.close()
