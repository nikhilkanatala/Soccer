import pandas  as pd
import matplotlib.pyplot as plt
import json
import os

# Load the data - path 'data/competitions.json'
# Navigate the folder '/Users/nikhilkanatala/Desktop/open-data/events' and load all the jsons in there

dir_path = '/Users/nikhilkanatala/Desktop/open-data/data/events/'
data = pd.DataFrame()
for file in os.listdir(dir_path)[:1]:
    path = os.path.join(dir_path, file)
    if os.path.isfile(path):
        data = pd.concat([data, pd.read_json(path)])

data = pd.concat([
    data.drop('possession_team', axis=1),
    pd.json_normalize(data['possession_team']).add_prefix('possession_team_')
], axis=1)

data.head()
data.columns

def time_to_minutes(time_str):
    minutes, seconds = map(int, time_str.split(':'))
    return minutes + (seconds/60)

vis_data = data[['id', 'index', 'period', 'minute', 'second', 'type', 'possession', 'possession_team_id', 'possession_team_name']]
vis_data['time'] = pd.to_datetime(vis_data['minute'] * 60 + vis_data['second'], unit='s').dt.strftime('%M:%S')
vis_data['minutes'] = vis_data['time'].apply(time_to_minutes)

x = vis_data['minutes'].to_numpy()
y = vis_data['possession_team_id'].to_numpy()

# calculate the total number of minutes each team had possession
team_possession = vis_data.sort_values(ascending=False, by='minutes')
print(team_possession[team_possession['possession_team_id'] == 226]['minutes'].to_list())

# things to do
# calculate the total number of minutes each team had possession
# plot a simple bar chart of the total number of minutes each team had possession