import pandas  as pd

# Load the data - path 'data/competitions.json'
data = pd.read_json('/Users/nikhilkanatala/Desktop/open-data/competitions.json')
data.head()