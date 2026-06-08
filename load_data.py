import sqlite3
import pandas as pd

# Loading CSV into pandas DataFrame
df=pd.read_csv('MOCK_DATA.csv')

df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')
df['amount'] = df['amount'].astype(str).str.replace('$', '', regex=False).astype(float)

# Connecting to SQLite to create a Database file
conn = sqlite3.connect('bloomberg_sim.db')

#Pushes DataFrame data into SQL table
df.to_sql('transactions', conn, if_exists='replace', index=False)

print("Database successfully created and populated!")

conn.close()