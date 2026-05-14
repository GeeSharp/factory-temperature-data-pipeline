import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

#Create Folders
plots_dir = Path("plots")
plots_dir.mkdir(exist_ok=True)

#Load data from SQLite
conn = sqlite3.connect("data/factory_data_v2.db")
df = pd.read_sql_query("SELECT * FROM temperature_readings",conn)
conn.close()

#Converts timestamp to datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])

#Plot temperature curve
plt.figure(figsize=(12,6))
plt.plot(df['timestamp'], df['temperature_c'], label="temperature (oC)")

#Highlight overheating
overheat = df[df['temperature_c'] > 38]
plt.scatter(overheat['timestamp'], overheat['temperature_c'], color='red', label="overheat")

#Customize plot
plt.title("Machine Temperature Trend")
plt.xlabel("Time")
plt.ylabel("Temperature (0C)")
plt.legend()
plt.grid(True)

#Save image
output_file = plots_dir / "temperature_plot.png"
plt.savefig(output_file, dpi=200)

print(f"Plot saved to {output_file}")