"""
IPL Cricket Statistics Analyzer
Main Application - Home Page
"""

import streamlit as st
import pandas as pd
import analysis as an
import visualizations as viz

# Page Configuration
st.set_page_config(
    page_title="IPL Stats Analyzer",
    page_icon="🏏",
    layout="wide"
)

# Load Data (cached)
@st.cache_data
def load_data():
    """Load and cache cricket data"""
    matches, deliveries = an.load_data()
    return matches, deliveries

# Load the data
matches_df, deliveries_df = load_data()

# Check if data is loaded
if matches_df is None or deliveries_df is None:
    st.error("⚠️ **Error: Data files not found!**")
    st.info("""
    Please download the IPL dataset and place the CSV files in the `data/` folder:
    - `data/matches.csv`
    - `data/deliveries.csv`
    
    See DATASET_INSTRUCTIONS.md for help.
    """)
    st.stop()

# ==================== HOME PAGE ====================

st.title("🏏 IPL Cricket Statistics Analyzer")
st.markdown("### Comprehensive Analysis of Indian Premier League (2008-2024)")

st.markdown("---")

# Quick Statistics
st.markdown("## 📊 Quick Statistics")

col1, col2, col3, col4 = st.columns(4)

with col1:
    total_matches = len(matches_df)
    st.metric("Total Matches", f"{total_matches:,}")

with col2:
    total_seasons = len(an.get_seasons(matches_df))
    st.metric("Seasons", total_seasons)

with col3:
    total_teams = len(an.get_all_teams(matches_df))
    st.metric("Teams", total_teams)

with col4:
    total_players = len(an.get_all_players(deliveries_df))
    st.metric("Players", f"{total_players:,}")

st.markdown("---")

# Overview Charts
st.markdown("## 📈 Overview")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Top 10 Run Scorers")
    batting_stats = an.get_top_run_scorers(deliveries_df, 10)
    viz.show_top_scorers(batting_stats, 10)

with col2:
    st.markdown("### Top 10 Wicket Takers")
    bowling_stats = an.get_top_wicket_takers(deliveries_df, 10)
    viz.show_top_bowlers(bowling_stats, 10)

st.markdown("---")

# Matches per Season
st.markdown("### Matches per Season")
season_matches = an.get_matches_by_season(matches_df)
viz.show_matches_per_season(season_matches)

st.markdown("---")

# Season Winners
st.markdown("### 🏆 IPL Champions by Season")
season_winners = an.get_season_winners(matches_df)
st.dataframe(season_winners, use_container_width=True, hide_index=True)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray;'>
    <p>IPL Cricket Statistics Analyzer | Built with Streamlit, Pandas, and NumPy</p>
    <p>Use the sidebar to navigate to different analysis pages →</p>
</div>
""", unsafe_allow_html=True)