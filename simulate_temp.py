import csv
import random
from datetime import datetime, timedelta
from pathlib import Path
#Make sure the "data" folder exists
data_dir = Path("data")
data_dir.mkdir(exist_ok=True)
#CVS file path
output_file = data_dir / "factory_temperature.csv"
#Simulation parameters
start_time = datetime.now().replace(microsecond=0)
num_points = 1000        # number of readings 
interval_seconds = 10    # seconds between readings

BASE_TEMP = 30.0         # base temperature (o C)
NOISE = 2.0              # random variation
# Overheating period
OVERHEAT_START_INDEX = 400
OVERHEAT_END_INDEX = 500
OVERHEAT_EXTRA = 10.0    #extra 0C during overheating

with open(output_file, mode="w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["timestamp", "machine_id", "temperature_c"])
    current_time = start_time
    for i in range(num_points):
        temp = BASE_TEMP + random.uniform(-NOISE, NOISE)
        # Add overheating in a time window
        if OVERHEAT_START_INDEX <= i <= OVERHEAT_END_INDEX:
            temp += OVERHEAT_EXTRA

        machine_id = "MACHINE_1"
        writer.writerow([
            current_time.isoformat(),
            machine_id,
            round(temp, 2)
        ])
        current_time += timedelta(seconds=interval_seconds)
print(f"Generated {num_points} rows → {output_file}") 