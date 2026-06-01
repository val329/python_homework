import sqlite3 
import pandas as pd

# connecting to the db
with sqlite3.connect("../db/lesson.db") as conn:
    sql_statement = """SELECT l.line_item_id, l.quantity, p.product_id, p.product_name, p.price FROM line_items l 
    JOIN products p ON l.product_id = p.product_id;"""

    # loading the results into a dataframe
    df = pd.read_sql_query(sql_statement, conn)
    print(df.head())

    # grouping, sorting and aggregations
    df['total'] = df['quantity'] * df['price']
    grouped_df = df.groupby("product_id").agg({"line_item_id":"count", "total":"sum", "product_name":"first"})
    grouped_df = grouped_df.sort_values(by="product_name")
    print(grouped_df.head())

    # exporting data to csv
    grouped_df.to_csv("order_summary.csv", sep=',', index=True, header=True, encoding=None)


