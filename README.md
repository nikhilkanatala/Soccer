# American Soccer Analysis ETL Pipeline

## Overview

This project implements an ETL (Extract, Transform, Load) pipeline to process data from the American Soccer Analysis (ASA) API and store it in an Azure database. The pipeline supports advanced analytics on team and player performance, salary trends, and match statistics. The project incorporates modular design principles to ensure scalability and adaptability for additional data sources or processing requirements.

---

## Project Structure

- **`python/`**: Contains Python scripts for data extraction, transformation, and orchestration.
  - `api.py`: Fetches data from ASA API endpoints.
  - `load.py`: Handles data cleaning, transformation, and loading into the Azure database.
  - `asa_etl.py`: Orchestrates the ETL process based on command-line arguments.
  - `db.py`: Manages database connections and data insertion processes.

- **`sql/`**: Contains SQL scripts for table creation and stored procedures.
  - `mls/`: Vendor-specific schema scripts.
    - `tables.sql`: Definitions for tables in the MLS schema.
  - `dbo/`: Aggregated data schema scripts.
    - `tables.sql`: Definitions for tables in the DBO schema.
    - `sprocs.sql`: Stored procedures to consolidated data.
  - `staging/`: Temporary schema scripts for data ingestion.
    - `tables.sql`: Definitions for staging tables.
    - `sprocs.sql`: Stored procedures for data loading.
---

## How to Use

### Prerequisites

1. **Python**: Install Python 3.8 or higher.
2. **Azure Database**: Set up an Azure SQL database and configure connection details.
3. **Dependencies**: Install required Python packages:
   ```bash
   pip install -r requirements.txt


# Setup and Configuration Guide

## Initial Setup

### Set Up Configurations
Update the `config.cfg` file with:
- Database credentials
- ASA API details

### Run ETL

Execute the ETL process using the following commands:

1. **Load data for a specific date range:**
   ```bash
   python asa_etl.py --load --start_date YYYY-MM-DD --end_date YYYY-MM-DD
   ```

2. **Load all available data:**
   ```bash
   python asa_etl.py --load-all
   ```

3. **Load historical data for a specific year:**
   ```bash
   python asa_etl.py --historical-load --year YYYY
   ```

## Scheduling

Set up a cron job to automate daily loads. For example, to run the script daily at 6:00 AM:

```bash
0 6 * * * /usr/bin/python3 /path/to/asa_etl.py --load
```

## Database Design

### Schemas

1. **MLS Schema**
   - Stores vendor-specific data
   - Includes games, xGoals, teams, and salaries

2. **STAGING Schema**
   - Handles temporary data ingestion
   - Manages data transformation

3. **DBO Schema**
   - Contains aggregated and processed data
   - Used for analysis and reporting

### Key Procedures

1. **DBO Schema Procedures**
   - `DBO.LOAD_GAME`: Consolidates game data into DBO schema
   - `DBO.LOAD_TEAM_SALARIES`: Aggregates team salary data for centralized analysis