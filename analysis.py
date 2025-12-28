"""
Cricket Statistics Analysis Functions
This module contains all the data analysis and statistical calculation functions
"""

import pandas as pd
import numpy as np


# ==================== DATA LOADING FUNCTIONS ====================

def load_data():
    """
    Load matches and deliveries data from CSV files
    
    Returns:
        tuple: (matches_df, deliveries_df)
    """
    try:
        matches = pd.read_csv('data/matches.csv')
        deliveries = pd.read_csv('data/deliveries.csv')
        return matches, deliveries
    except FileNotFoundError:
        return None, None


# ==================== PLAYER STATISTICS FUNCTIONS ====================

def get_batting_stats(deliveries_df, player_name=None):
    """
    Calculate batting statistics for a player or all players
    
    Parameters:
        deliveries_df: DataFrame with ball-by-ball data
        player_name: Specific player name (optional)
    
    Returns:
        DataFrame with batting statistics
    """
    # Filter for specific player if provided
    if player_name:
        player_data = deliveries_df[deliveries_df['batter'] == player_name]
    else:
        player_data = deliveries_df
    
    # Calculate total runs scored by each batsman
    total_runs = player_data.groupby('batter')['batsman_runs'].sum()
    
    # Calculate number of balls faced (excluding wides which are not counted as balls faced)
    balls_faced = player_data[player_data['extras_type'] != 'wides'].groupby('batter').size()
    
    # Calculate strike rate (runs per 100 balls)
    strike_rate = (total_runs / balls_faced * 100).round(2)
    
    # Calculate number of innings
    innings = player_data.groupby('batter')['match_id'].nunique()
    
    # Calculate average (total runs / innings) - handle division by zero
    average = (total_runs / innings).round(2)
    average = average.replace([np.inf, -np.inf], 0)
    
    # Count boundaries (4s and 6s)
    fours = player_data[player_data['batsman_runs'] == 4].groupby('batter').size()
    sixes = player_data[player_data['batsman_runs'] == 6].groupby('batter').size()
    
    # Combine all stats into a DataFrame
    batting_stats = pd.DataFrame({
        'Player': total_runs.index,
        'Innings': innings.reindex(total_runs.index, fill_value=0).values,
        'Total_Runs': total_runs.values,
        'Average': average.reindex(total_runs.index, fill_value=0).values,
        'Strike_Rate': strike_rate.reindex(total_runs.index, fill_value=0).values,
        'Balls_Faced': balls_faced.reindex(total_runs.index, fill_value=0).values,
        'Fours': fours.reindex(total_runs.index, fill_value=0).values,
        'Sixes': sixes.reindex(total_runs.index, fill_value=0).values
    })
    
    # Sort by total runs
    batting_stats = batting_stats.sort_values('Total_Runs', ascending=False)
    
    return batting_stats


def get_bowling_stats(deliveries_df, player_name=None):
    """
    Calculate bowling statistics for a player or all players
    
    Parameters:
        deliveries_df: DataFrame with ball-by-ball data
        player_name: Specific player name (optional)
    
    Returns:
        DataFrame with bowling statistics
    """
    # Filter for specific player if provided
    if player_name:
        player_data = deliveries_df[deliveries_df['bowler'] == player_name]
    else:
        player_data = deliveries_df
    
    # Calculate total wickets taken
    wickets = player_data[player_data['is_wicket'] == 1].groupby('bowler').size()
    
    # Calculate total runs conceded
    runs_conceded = player_data.groupby('bowler')['total_runs'].sum()
    
    # Calculate balls bowled (excluding wides and noballs as they don't count as legal deliveries)
    # Wides and noballs are in extras_type column
    legal_deliveries = player_data[~player_data['extras_type'].isin(['wides', 'noballs'])]
    balls_bowled = legal_deliveries.groupby('bowler').size()
    
    # Calculate overs bowled
    overs_bowled = (balls_bowled / 6).round(1)
    
    # Calculate economy rate (runs per over) - handle division by zero
    economy = (runs_conceded / overs_bowled).round(2)
    economy = economy.replace([np.inf, -np.inf], 0)
    
    # Calculate bowling average (runs per wicket) - handle division by zero
    bowling_avg = (runs_conceded / wickets).round(2)
    bowling_avg = bowling_avg.replace([np.inf, -np.inf], 0)
    
    # Calculate number of matches
    matches = player_data.groupby('bowler')['match_id'].nunique()
    
    # Combine all stats
    bowling_stats = pd.DataFrame({
        'Player': wickets.index,
        'Matches': matches.reindex(wickets.index, fill_value=0).values,
        'Wickets': wickets.values,
        'Runs_Conceded': runs_conceded.reindex(wickets.index, fill_value=0).values,
        'Overs': overs_bowled.reindex(wickets.index, fill_value=0).values,
        'Economy': economy.reindex(wickets.index, fill_value=0).values,
        'Average': bowling_avg.reindex(wickets.index, fill_value=0).values
    })
    
    # Sort by wickets
    bowling_stats = bowling_stats.sort_values('Wickets', ascending=False)
    
    return bowling_stats


def get_top_run_scorers(deliveries_df, n=10):
    """
    Get top N run scorers
    
    Parameters:
        deliveries_df: DataFrame with ball-by-ball data
        n: Number of top scorers (default: 10)
    
    Returns:
        DataFrame with top scorers
    """
    batting_stats = get_batting_stats(deliveries_df)
    return batting_stats.head(n)


def get_top_wicket_takers(deliveries_df, n=10):
    """
    Get top N wicket takers
    
    Parameters:
        deliveries_df: DataFrame with ball-by-ball data
        n: Number of top wicket takers (default: 10)
    
    Returns:
        DataFrame with top wicket takers
    """
    bowling_stats = get_bowling_stats(deliveries_df)
    return bowling_stats.head(n)


# ==================== TEAM STATISTICS FUNCTIONS ====================

def get_team_stats(matches_df):
    """
    Calculate statistics for all teams
    
    Parameters:
        matches_df: DataFrame with match-level data
    
    Returns:
        DataFrame with team statistics
    """
    # Count total matches played by each team
    team1_matches = matches_df['team1'].value_counts()
    team2_matches = matches_df['team2'].value_counts()
    total_matches = team1_matches.add(team2_matches, fill_value=0)
    
    # Count wins for each team
    wins = matches_df['winner'].value_counts()
    
    # Calculate win percentage
    win_percentage = (wins / total_matches * 100).round(2)
    
    # Combine stats
    team_stats = pd.DataFrame({
        'Team': total_matches.index,
        'Matches_Played': total_matches.values,
        'Wins': wins.reindex(total_matches.index, fill_value=0).values,
        'Win_Percentage': win_percentage.reindex(total_matches.index, fill_value=0).values
    })
    
    # Sort by wins
    team_stats = team_stats.sort_values('Wins', ascending=False)
    
    return team_stats


def get_team_performance_by_season(matches_df, team_name):
    """
    Get season-wise performance for a specific team
    
    Parameters:
        matches_df: DataFrame with match-level data
        team_name: Name of the team
    
    Returns:
        DataFrame with season-wise stats
    """
    # Filter matches involving the team
    team_matches = matches_df[(matches_df['team1'] == team_name) | (matches_df['team2'] == team_name)]
    
    # Group by season
    season_stats = team_matches.groupby('season').agg({
        'id': 'count',  # Total matches
        'winner': lambda x: (x == team_name).sum()  # Wins
    }).reset_index()
    
    season_stats.columns = ['Season', 'Matches', 'Wins']
    season_stats['Win_Rate'] = (season_stats['Wins'] / season_stats['Matches'] * 100).round(2)
    
    return season_stats


def get_head_to_head(matches_df, team1, team2):
    """
    Get head-to-head record between two teams
    
    Parameters:
        matches_df: DataFrame with match-level data
        team1: First team name
        team2: Second team name
    
    Returns:
        Dictionary with head-to-head stats
    """
    # Filter matches between these two teams
    h2h_matches = matches_df[
        ((matches_df['team1'] == team1) & (matches_df['team2'] == team2)) |
        ((matches_df['team1'] == team2) & (matches_df['team2'] == team1))
    ]
    
    # Count wins
    team1_wins = h2h_matches[h2h_matches['winner'] == team1].shape[0]
    team2_wins = h2h_matches[h2h_matches['winner'] == team2].shape[0]
    total_matches = h2h_matches.shape[0]
    
    return {
        'total_matches': total_matches,
        f'{team1}_wins': team1_wins,
        f'{team2}_wins': team2_wins,
        'ties': total_matches - team1_wins - team2_wins
    }


# ==================== MATCH STATISTICS FUNCTIONS ====================

def get_matches_by_season(matches_df):
    """
    Get number of matches played in each season
    
    Parameters:
        matches_df: DataFrame with match-level data
    
    Returns:
        Series with season-wise match counts
    """
    return matches_df['season'].value_counts().sort_index()


def get_venue_stats(matches_df):
    """
    Get statistics for each venue
    
    Parameters:
        matches_df: DataFrame with match-level data
    
    Returns:
        DataFrame with venue statistics
    """
    venue_stats = matches_df.groupby('venue').agg({
        'id': 'count',  # Total matches
    }).reset_index()
    
    venue_stats.columns = ['Venue', 'Matches_Played']
    venue_stats = venue_stats.sort_values('Matches_Played', ascending=False)
    
    return venue_stats


def get_toss_impact(matches_df):
    """
    Analyze impact of toss on match results
    
    Parameters:
        matches_df: DataFrame with match-level data
    
    Returns:
        Dictionary with toss impact statistics
    """
    # Count matches where toss winner also won the match
    toss_and_match_win = matches_df[matches_df['toss_winner'] == matches_df['winner']].shape[0]
    total_matches = matches_df.shape[0]
    
    win_percentage = round((toss_and_match_win / total_matches * 100), 2)    
    return {
        'total_matches': total_matches,
        'toss_winner_won_match': toss_and_match_win,
        'win_percentage': win_percentage
    }


def get_season_winners(matches_df):
    """
    Get the winner of each IPL season
    
    Parameters:
        matches_df: DataFrame with match-level data
    
    Returns:
        DataFrame with season winners
    """
    # Filter for final matches (usually the last match of each season)
    # Group by season and get the last match (final)
    season_finals = matches_df.sort_values('date').groupby('season').last()
    
    season_winners = pd.DataFrame({
        'Season': season_finals.index,
        'Winner': season_finals['winner'].values,
        'Venue': season_finals['venue'].values
    })
    
    return season_winners


# ==================== UTILITY FUNCTIONS ====================

def get_all_players(deliveries_df):
    """
    Get list of all unique players
    
    Parameters:
        deliveries_df: DataFrame with ball-by-ball data
    
    Returns:
        Sorted list of player names
    """
    batters = set(deliveries_df['batter'].unique())
    bowlers = set(deliveries_df['bowler'].unique())
    all_players = sorted(list(batters.union(bowlers)))
    
    return all_players


def get_all_teams(matches_df):
    """
    Get list of all unique teams
    
    Parameters:
        matches_df: DataFrame with match-level data
    
    Returns:
        Sorted list of team names
    """
    teams1 = set(matches_df['team1'].unique())
    teams2 = set(matches_df['team2'].unique())
    all_teams = sorted(list(teams1.union(teams2)))
    
    return all_teams


def get_seasons(matches_df):
    """
    Get list of all seasons
    
    Parameters:
        matches_df: DataFrame with match-level data
    
    Returns:
        Sorted list of seasons
    """
    return sorted(matches_df['season'].unique())