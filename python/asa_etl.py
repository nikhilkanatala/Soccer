"""
American Soccer Analysis ETL 
"""

import argparse
import os
import logging
from datetime import datetime, timedelta
from modules.asa_api.load import load, load_all, historical_load

LOG_FILE_PATH = os.path.join(os.path.expanduser('~'), 'project.log')

PARSER = argparse.ArgumentParser(description='American Soccer Analysis ETL Tasks')

PARSER.add_argument('--load', action="store_true",
                        dest='load', help="Load data from api to tables")
PARSER.add_argument('--load-all', action="store_true",
                        dest='load_all', help="Load all data from api to tables")
PARSER.add_argument('--historical-load', action="store_true",
                        dest='historical_load', help="Load historical data from api to tables")
PARSER.add_argument('--start_date', type=str, 
                        dest='start_date', help="Start date for daily load")
PARSER.add_argument('--end_date', type=str,
                        dest='end_date', help="End date for daily load")
PARSER.add_argument('--year', type=int,
                        dest='year', help="Year for historical load")

ARGS = PARSER.parse_args()

def main():
    """
    Main function
    """
    
    logging.basicConfig(filename=LOG_FILE_PATH, level=logging.INFO)
    logging.info('Starting ETL...')

    if ARGS.load:
        # If no start_date and end_date are provided, load data for the last 2 days
        if not ARGS.start_date and not ARGS.end_date:
            end_date = datetime.now().strftime('%Y-%m-%d')
            start_date = (datetime.now() - timedelta(days=2)).strftime('%Y-%m-%d')
        else:
            start_date = ARGS.start_date
            end_date = ARGS.end_date
        
        # Load data            
        load(start_date, end_date)

    if ARGS.load_all:
        # Load all data
        load_all()

    if ARGS.historical_load:
        # Load historical data
        # Historical data takes year as input
        historical_load(ARGS.year)

if __name__ == '__main__':
    # main()
    load(start_date='2024-12-05', end_date='2024-12-08')