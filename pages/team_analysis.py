"""
Team Performance Analysis Page
"""

import streamlit as st
import analysis as an
import visualizations as viz

st.set_page_config(page_title="Team Stats", page_icon="🏆", layout="wide")

# Load data
@st.cache_data
def load_data():
    return an.load_data()

matches_df, deliveries_df = load_data()

if matches_df is None or deliveries_df is None:
    st.error("⚠️ Data files not found!")
    st.stop()

# ==================== TEAM ANALYSIS PAGE ====================

st.title("🏆 Team Performance Analysis")

# Get all teams
all_teams = an.get_all_teams(matches_df)

# Team selection
selected_team = st.selectbox("Select a Team", all_teams, index=0)

st.markdown("---")

# Overall team stats
team_stats = an.get_team_stats(matches_df)
selected_team_stats = team_stats[team_stats['Team'] == selected_team]

if not selected_team_stats.empty:
    st.markdown(f"### Overall Performance - {selected_team}")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Matches Played", int(selected_team_stats['Matches_Played'].values[0]))
    with col2:
        st.metric("Wins", int(selected_team_stats['Wins'].values[0]))
    with col3:
        losses = int(selected_team_stats['Matches_Played'].values[0] - selected_team_stats['Wins'].values[0])
        st.metric("Losses", losses)
    with col4:
        st.metric("Win %", f"{selected_team_stats['Win_Percentage'].values[0]:.2f}%")

st.markdown("---")

# Season-wise performance
st.markdown(f"### Season-wise Performance - {selected_team}")
season_performance = an.get_team_performance_by_season(matches_df, selected_team)

col1, col2 = st.columns([2, 1])

with col1:
    # Line chart
    viz.show_season_performance(season_performance, selected_team)

with col2:
    # Display data table
    st.dataframe(season_performance, use_container_width=True, hide_index=True, height=400)

st.markdown("---")

# All teams comparison
st.markdown("### 📊 All Teams Comparison")

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### Team Statistics Table")
    st.dataframe(team_stats, use_container_width=True, hide_index=True)

with col2:
    st.markdown("#### Top Teams by Wins")
    top_teams = team_stats.head(8)[['Team', 'Wins']].set_index('Team')
    st.bar_chart(top_teams)

st.markdown("---")

# Head to Head
st.markdown("### ⚔️ Head-to-Head Comparison")

col1, col2 = st.columns(2)

with col1:
    team1 = st.selectbox("Team 1", all_teams, index=0, key='team1')
with col2:
    team2 = st.selectbox("Team 2", all_teams, index=1, key='team2')

if team1 != team2:
    h2h_stats = an.get_head_to_head(matches_df, team1, team2)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Matches", h2h_stats['total_matches'])
    with col2:
        st.metric(f"{team1} Wins", h2h_stats[f'{team1}_wins'])
    with col3:
        st.metric(f"{team2} Wins", h2h_stats[f'{team2}_wins'])
    
    # Head to head chart
    viz.show_head_to_head(h2h_stats, team1, team2)
else:
    st.warning("Please select two different teams for comparison.")