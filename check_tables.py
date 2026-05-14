import sqlite3
conn = sqlite3.connect("data/factory_data_v2.db")
cur = conn.cursor()
cur.execute("SELECT name FROM sqlite_master WHERE type='table';")  
print(cur.fetchall())
conn.close()