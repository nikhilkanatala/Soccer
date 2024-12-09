"""
Mapping for the raw columns to Azure DB
"""

GAME_COLS = {
    'game_id': 'GAME_ID',
    'date_time_utc': 'DATE_TIME_UTC',
    'home_score': 'HOME_SCORE',
    'away_score': 'AWAY_SCORE',
    'home_team_id': 'HOME_TEAM_ID',
    'away_team_id': 'AWAY_TEAM_ID',
    'referee_id': 'REFEREE_ID',
    'stadium_id': 'STADIUM_ID',
    'home_manager_id': 'HOME_MANAGER_ID',
    'away_manager_id': 'AWAY_MANAGER_ID',
    'expanded_minutes': 'EXPANDED_MINUTES',
    'season_name': 'SEASON_NAME',
    'matchday': 'MATCHDAY',
    'attendance': 'ATTENDANCE',
    'knockout_game': 'KNOCKOUT_GAME',
    'last_updated_utc': 'LAST_UPDATED_UTC'
}

GAME_XGOAL_COLS = {
    'game_id': 'GAME_ID',
    'date_time_utc': 'DATE_TIME_UTC',
    'home_team_id': 'HOME_TEAM_ID',
    'home_goals': 'HOME_GOALS',
    'home_team_xgoals': 'HOME_TEAM_XGOALS',
    'home_player_xgoals': 'HOME_PLAYER_XGOALS',
    'away_team_id': 'AWAY_TEAM_ID',
    'away_goals': 'AWAY_GOALS',
    'away_team_xgoals': 'AWAY_TEAM_XGOALS',
    'away_player_xgoals': 'AWAY_PLAYER_XGOALS',
    'goal_difference': 'GOAL_DIFFERENCE',
    'team_xgoal_difference': 'TEAM_XGOAL_DIFFERENCE',
    'player_xgoal_difference': 'PLAYER_XGOAL_DIFFERENCE',
    'final_score_difference': 'FINAL_SCORE_DIFFERENCE',
    'home_xpoints': 'HOME_XPOINTS',
    'away_xpoints': 'AWAY_XPOINTS'
}
