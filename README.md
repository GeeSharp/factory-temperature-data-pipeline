# factory-temperature-data-pipeline - Project 1
## Overview
This project simulates industrial machine temperature sensor data and  demostrates a basic ETL workflow for Industrial IoT Predictive maintenance applications.
Simulated industrial temperature sensor ETL pipeline using Python, CSV, SQLite, and SQL analysis for industrial IoT and predictive maintenance concepts. 
## Pipeline
1. Generate time-series temperature data using Python
2. Store readings in a CSV file
3. Load data into a SQLite database
4. Run SQL queries for analysis and overheating detection
5. Visualize temperature trends

## Tech Stack
- Python
- SQLite
- SQL
- CSV
- Matplotlib

## Files
- `simulate_temp.py` → generates temperature data
- `load_to_db.py` → imports CSV into SQLite
- `run_queries.py` → executes SQL analysis
- `visualize.py` → generates plots
- `queries.sql` → SQL queries
- `data/` → generated data
- `plots/` → visualization outputs

## Future Improvements
- Real-time sensor streaming
- MQTT integration
- Cloud database support
- Power BI dashboard
- Predictive analytics models
