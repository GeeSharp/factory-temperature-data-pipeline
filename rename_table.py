import sqlite3
conn = sqlite3.connect("data/factory_data.db")
cur = conn.cursor()

cur.execute("ALTER TABLE TEMPERATURE_readings RENAME TO temperature_readings;")
conn.commit()
conn.close()


print("Table Renamed successfuly")                                                                                                
