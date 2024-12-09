"""
Config Info Wrapper
"""

import os
import logging
from configparser import ConfigParser

# Path to config file
# Please update this path to the location of your config file
CONFIG_PATH = os.path.join(os.path.expanduser('~'),'config.cfg')

def get_config(section):
    """
    Get config info for the requested section.
    """
    
    config = ConfigParser()
    logging.info(f"Reading config...")
    config.read(CONFIG_PATH)
    
    return config[section]
