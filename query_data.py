import sqlite3
import pandas as pd

conn = sqlite3.connect('bloomberg_sim.db')

#SQL query to aggregate monthly performance for each merchant
sql_query = """
SELECT 
    merchant,
    strftime('%Y-%m', date) AS transaction_month,
    COUNT(DISTINCT user_id) AS unique_customers,
    SUM(amount) AS total_revenue,
    AVG(amount) AS avg_transaction_value
FROM transactions
GROUP BY merchant, transaction_month
ORDER BY transaction_month ASC, total_revenue DESC;
"""

# Pandas runs the query and formats it into a DataFrame
analyzed_df = pd.read_sql_query(sql_query, conn)

# Aggregate data is saved to CSV
analyzed_df.to_csv('monthly_merchant_trends.csv', index=False)

print("SQL Query executed successfully! 'monthly_merchant_trends.csv' has been created.")

# Close the connection
conn.close()