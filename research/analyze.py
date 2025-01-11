import pandas  as pd
import os

# Load the data - path 'data/competitions.json'
# Navigate the folder '/Users/nikhilkanatala/Desktop/open-data/events' and load all the jsons in there

dir_path = '/Users/nikhilkanatala/Desktop/open-data/data/events/'
data = pd.DataFrame()
for file in os.listdir(dir_path):
    path = os.path.join(dir_path, file)
    if os.path.isfile(path):
        data = pd.concat([data, pd.read_json(path)])

data.head()