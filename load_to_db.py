import sqlite3
import csv
from pathlib import Path

#path to files  yes
data_dir = Path("data")
csv_file = data_dir /"factory_temperature.csv"
db_file = data_dir /"factory_data_v2.db"

#Connect to SQLite database
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

#Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS temperature_readings (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               timestamp TEXT NOT NULL,
               machine_id TEXT NOT NULL,
               temperature_c REAL NOT NULL
);
""")

#Clear existing data
# Remove existing data (optional, keeps your DB clean)
cursor.execute("DELETE FROM temperature_readings;")

# Read CVS
with open(csv_file, newline="") as f:
    reader = csv.DictReader(f)
    rows = [
        (row["timestamp"], row["machine_id"], float(row["temperature_c"]))
        for row in reader
    ]
    #Insert data into database
    cursor.executemany("""
    INSERT INTO temperature_readings (timestamp, machine_id, temperature_c)
    VALUES (?, ?, ?);
    """,rows)

    conn.commit()
    conn.close()

    print(f"Loaded {len(rows)} rows into {db_file}")