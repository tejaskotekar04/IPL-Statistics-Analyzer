"""
Cricket Statistics Visualization Functions
This module contains chart creation functions using Streamlit's native charts
"""

import streamlit as st
import pandas as pd


def show_top_scorers(batting_stats_df, n=10):
    """
    Display bar chart of top run scorers using Streamlit
    
    Parameters:
        batting_stats_df: DataFrame with batting statistics
        n: Number of top scorers to display
    """
    top_scorers = batting_stats_df.head(n)[['Player', 'Total_Runs']]
    top_scorers = top_scorers.set_index('Player')
    st.bar_chart(top_scorers)


def show_top_bowlers(bowling_stats_df, n=10):
    """
    Display bar chart of top wicket takers using Streamlit
    
    Parameters:
        bowling_stats_df: DataFrame with bowling statistics
        n: Number of top bowlers to display
    """
    top_bowlers = bowling_stats_df.head(n)[['Player', 'Wickets']]
    top_bowlers = top_bowlers.set_index('Player')
    st.bar_chart(top_bowlers)


def show_season_performance(season_data, team_name):
    """
    Display line chart of team performance over seasons using Streamlit
    
    Parameters:
        season_data: DataFrame with season-wise performance
        team_name: Name of the team
    """
    chart_data = season_data.set_index('Season')[['Wins', 'Matches']]
    st.line_chart(chart_data)


def show_matches_per_season(season_matches):
    """
    Display bar chart of matches per season using Streamlit
    
    Parameters:
        season_matches: Series with season-wise match counts
    """
    df = pd.DataFrame({
        'Season': season_matches.index,
        'Matches': season_matches.values
    })
    df = df.set_index('Season')
    st.bar_chart(df)


def show_player_comparison(comparison_data):
    """
    Display bar chart for player comparison using Streamlit
    
    Parameters:
        comparison_data: DataFrame with player statistics
    """
    # Show Total Runs comparison
    st.markdown("#### Total Runs")
    runs_data = comparison_data.set_index('Player')[['Total_Runs']]
    st.bar_chart(runs_data)
    
    # Show Strike Rate comparison
    st.markdown("#### Strike Rate")
    sr_data = comparison_data.set_index('Player')[['Strike_Rate']]
    st.bar_chart(sr_data)


def show_head_to_head(h2h_data, team1, team2):
    """
    Display head-to-head comparison using Streamlit
    
    Parameters:
        h2h_data: Dictionary with head-to-head statistics
        team1: First team name
        team2: Second team name
    """
    df = pd.DataFrame({
        'Team': [team1, team2, 'Ties/NR'],
        'Wins': [h2h_data[f'{team1}_wins'], h2h_data[f'{team2}_wins'], h2h_data['ties']]
    })
    df = df.set_index('Team')
    st.bar_chart(df)