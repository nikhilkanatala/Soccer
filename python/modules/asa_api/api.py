"""
Accessing American Soccer Analysis's API
"""

import requests
from urllib.error import HTTPError
import pandas as pd
import logging

# Base URL for the American Soccer Analysis API and MLS in particular
MLS_BASE_URL = "https://app.americansocceranalysis.com/api/v1/mls/"

# Different endpoints available through the API listed by category
END_POINTS = {
    'games': [
        'games',
        'games/xgoals'
    ],
    'players': [
        'players',
        'players/xgoals',
        'players/xpass',
        'players/goals-added',
        'players/salaries'
    ],
    'teams': [
        'teams',
        'teams/xgoals',
        'teams/xpass',
        'teams/goals-added',
        'teams/salaries'
    ]   
}

def get_games(year=None, game_id=None):
    """
    Get all games for a given season or game_id
    """
    logging.info(f"Fetching games...")
    url = MLS_BASE_URL + END_POINTS['games'][0]
    response = requests.get(
        url,
        params={
            'season_name': year,
            'game_id': game_id
        }
    )
    
    # catch bad requests
    if response.status_code != 200:
        msg = f"Bad HTTP response code: {response.status_code}, received {response.text}"
        logging.error(msg)
        raise HTTPError(url, response.status_code, msg, None, None)

    df_games = pd.json_normalize(response.json())
    logging.info(f"Games retrieved: {df_games.shape[0]}")

    return df_games

def get_game_xgoals(start_date = None, end_date = None, year = None, game_id = None):
    """
    Get all games and expected goals for a given season or game_id and/or date range
    """
    logging.info(f"Fetching games and expected goals...")
    if (start_date and not end_date) or (end_date and not start_date):
        msg = f'''
        The API requires the following parameters to be set: start_date, end_date.
        Please set these parameters as expected or try other parameters (year, game_id)
        '''
        logging.error(msg)
        raise ValueError(msg)
    
    url = MLS_BASE_URL + END_POINTS['games'][1]
    response = requests.get(
        url,
        params={
            'season_name': year,
            'game_id': game_id,
            'start_date': start_date,
            'end_date': end_date
        }
    )
    
    # catch bad requests
    if response.status_code != 200:
        msg = f"Bad HTTP response code: {response.status_code}, received {response.text}"
        logging.error(msg)
        raise HTTPError(url, response.status_code, msg, None, None)

    df_games = pd.json_normalize(response.json())
    logging.info(f"Games and expected goals retrieved: {df_games.shape[0]}")

    return df_games

def get_teams(team_id=None):
    """
    Get all teams for a given season or team_id
    """
    logging.info(f"Fetching teams...")
    url = MLS_BASE_URL + END_POINTS['teams'][0]
    response = requests.get(
        url,
        params={
            'team_id': team_id
        }
    )
    
    # catch bad requests
    if response.status_code != 200:
        msg = f"Bad HTTP response code: {response.status_code}, received {response.text}"
        logging.error(msg)
        raise HTTPError(url, response.status_code, msg, None, None)

    df_teams = pd.json_normalize(response.json())
    logging.info(f"Teams retrieved: {df_teams.shape[0]}")
    
    return df_teams

def get_team_salaries(split_by='teams', year=None, team_id=None):
    """
    Get all team salaries for a given season.
    Or get a team's salaries for a given season and team_id.
    split_by can be 'teams' or 'positions'. 
    Default is 'teams' as we are interested in team salaries.
    """
    logging.info(f"Fetching team salaries...")
    url = MLS_BASE_URL + END_POINTS['teams'][4]        
    response = requests.get(
        url,
        params={
            'season_name': year,
            'team_id': team_id,
            'split_by_teams': split_by == 'teams',
            'split_by_seasons': True, # always split by seasons for now, can be modified later
            'split_by_positions': split_by == 'positions'
        }
    )
    
    # catch bad requests
    if response.status_code != 200:
        msg = f"Bad HTTP response code: {response.status_code}, received {response.text}"
        logging.error(msg)
        raise HTTPError(url, response.status_code, msg, None, None)

    df_team_salaries = pd.json_normalize(response.json())
    logging.info(f"Team salaries retrieved: {df_team_salaries.shape[0]}")

    return df_team_salaries

def get_players(player_id=None):
    """
    Get player info for a given season or player_id
    """
    logging.info(f"Fetching players...")
    url = MLS_BASE_URL + END_POINTS['players'][0]
    response = requests.get(
        url,
        params={
            'player_id': player_id
        }
    )
    
    # catch bad requests
    if response.status_code != 200:
        msg = f"Bad HTTP response code: {response.status_code}, received {response.text}"
        logging.error(msg)
        raise HTTPError(url, response.status_code, msg, None, None)

    df_players = pd.json_normalize(response.json())
    logging.info(f"Players retrieved: {df_players.shape[0]}")
    return df_players

def get_player_xgoals(start_date = None, end_date = None, year=None, player_id=None):
    """
    Get player expected goals for a given season or player_id and/or date range
    """
    logging.info(f"Fetching player expected goals...")
    if (start_date and not end_date) or (end_date and not start_date):
        msg = f'''
        The API requires the following parameters to be set: start_date, end_date.
        Please set these parameters as expected or try other parameters (year, player_id)
        '''
        logging.error(msg)
        raise ValueError(msg)
    
    url = MLS_BASE_URL + END_POINTS['players'][1]
    response = requests.get(
        url,
        params={
            'season_name': year,
            'player_id': player_id,
            'start_date': start_date,
            'end_date': end_date
        }
    )
    
    # catch bad requests
    if response.status_code != 200:
        msg = f"Bad HTTP response code: {response.status_code}, received {response.text}"
        logging.error(msg)
        raise HTTPError(url, response.status_code, msg, None, None)

    df_player_xgoals = pd.json_normalize(response.json())
    logging.info(f"Player expected goals retrieved: {df_player_xgoals.shape[0]}")
    return df_player_xgoals

def get_player_xpass(start_date = None, end_date = None, year=None, player_id=None):
    """
    Get player expected assists for a given season or player_id and/or date range
    """
    logging.info(f"Fetching player expected assists...")
    if (start_date and not end_date) or (end_date and not start_date):
        msg = f'''
        The API requires the following parameters to be set: start_date, end_date.
        Please set these parameters as expected or try other parameters (year, player_id)
        '''
        logging.error(msg)
        raise ValueError(msg)
    
    url = MLS_BASE_URL + END_POINTS['players'][2]
    response = requests.get(
        url,
        params={
            'season_name': year,
            'player_id': player_id,
            'start_date': start_date,
            'end_date': end_date
        }
    )
    
    # catch bad requests
    if response.status_code != 200:
        msg = f"Bad HTTP response code: {response.status_code}, received {response.text}"
        logging.error(msg)
        raise HTTPError(url, response.status_code, msg, None, None)

    df_player_xpass = pd.json_normalize(response.json())
    logging.info(f"Player expected assists retrieved: {df_player_xpass.shape[0]}")
    return df_player_xpass

def get_player_salaries(start_date = None, end_date = None, year=None, position=None, player_id=None):
    """
    Get player salaries for a given season or player_id and/or date range
    """
    logging.info(f"Fetching player salaries...")
    if (start_date and not end_date) or (end_date and not start_date):
        msg = f'''
        The API requires the following parameters to be set: start_date, end_date.
        Please set these parameters as expected or try other parameters (year, player_id)
        '''
        logging.error(msg)
        raise ValueError(msg)
    
    url = MLS_BASE_URL + END_POINTS['players'][4]
    response = requests.get(
        url,
        params={
            'season_name': year,
            'player_id': player_id,
            'start_date': start_date,
            'end_date': end_date,
            'position': position
        }
    )
    
    # catch bad requests
    if response.status_code != 200:
        msg = f"Bad HTTP response code: {response.status_code}, received {response.text}"
        logging.error(msg)
        raise HTTPError(url, response.status_code, msg, None, None)

    df_player_salaries = pd.json_normalize(response.json())
    logging.info(f"Player salaries retrieved: {df_player_salaries.shape[0]}")
    return df_player_salaries

def get_referees():
    """
    Get all referees
    """
    logging.info(f"Fetching referees...")
    url = MLS_BASE_URL + 'referees'
    response = requests.get(url)
    
    # catch bad requests
    if response.status_code != 200:
        msg = f"Bad HTTP response code: {response.status_code}, received {response.text}"
        logging.error(msg)
        raise HTTPError(url, response.status_code, msg, None, None)

    df_referees = pd.json_normalize(response.json())
    logging.info(f"Referees retrieved: {df_referees.shape[0]}")
    return df_referees

def get_managers():
    """
    Get all managers
    """
    logging.info(f"Fetching managers...")
    url = MLS_BASE_URL + 'managers'
    response = requests.get(url)
    
    # catch bad requests
    if response.status_code != 200:
        msg = f"Bad HTTP response code: {response.status_code}, received {response.text}"
        logging.error(msg)
        raise HTTPError(url, response.status_code, msg, None, None)

    df_managers = pd.json_normalize(response.json())
    logging.info(f"Managers retrieved: {df_managers.shape[0]}")

    return df_managers

def get_stadiums():
    """
    Get all stadiums
    """
    logging.info(f"Fetching stadiums...")

    url = MLS_BASE_URL + 'stadia'
    response = requests.get(url)
    
    # catch bad requests
    if response.status_code != 200:
        msg = f"Bad HTTP response code: {response.status_code}, received {response.text}"
        logging.error(msg)
        raise HTTPError(url, response.status_code, msg, None, None)

    df_stadiums = pd.json_normalize(response.json())
    logging.info(f"Stadiums retrieved: {df_stadiums.shape[0]}")

    return df_stadiums
