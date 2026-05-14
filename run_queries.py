import sqlite3

conn = sqlite3.connect("data/factory_data.db") 
cursor = conn.cursor()  

#Total rows
cursor.execute("SELECT COUNT(*) FROM temperature_readings;")
print("Total rows:", cursor.fetchall()) 

#Min, Max, Avg temperature 
cursor.execute("SELECT MIN(temperature_c), MAX(temperature_c),AVG(temperature_c) FROM temperature_readings;")         
print("Min, Max, Avg:", cursor.fetchall())

#Top 10 hottest readings
cursor.execute(""" 
SELECT timestamp, machine_id, temperature_c
FROM temperature_readings 
ORDER BY temperature_c DESC
LIMIT 10;
""")   
print("Top 10 hottest readings:")
for row in cursor.fetchall():
    print(row)

conn.close()                                                                                                                                                                                                                                             