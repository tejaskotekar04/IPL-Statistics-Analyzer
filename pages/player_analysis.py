"""
Player Statistics Page
"""

import streamlit as st
import analysis as an

st.set_page_config(page_title="Player Stats", page_icon="👤", layout="wide")

# Load data
@st.cache_data
def load_data():
    return an.load_data()

matches_df, deliveries_df = load_data()

if matches_df is None or deliveries_df is None:
    st.error("⚠️ Data files not found!")
    st.stop()

# ==================== PLAYER ANALYSIS PAGE ====================

st.title("👤 Player Statistics")

# Get all players
all_players = an.get_all_players(deliveries_df)

# Player selection
selected_player = st.selectbox("Select a Player", all_players, index=0)

st.markdown("---")

# Create tabs for batting and bowling
tab1, tab2 = st.tabs(["🏏 Batting Statistics", "⚾ Bowling Statistics"])

with tab1:
    st.markdown(f"### Batting Performance - {selected_player}")
    
    # Get batting stats
    player_batting = an.get_batting_stats(deliveries_df, selected_player)
    
    if not player_batting.empty:
        # Display metrics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Runs", f"{int(player_batting['Total_Runs'].values[0]):,}")
        with col2:
            st.metric("Average", f"{player_batting['Average'].values[0]:.2f}")
        with col3:
            st.metric("Strike Rate", f"{player_batting['Strike_Rate'].values[0]:.2f}")
        with col4:
            st.metric("Innings", int(player_batting['Innings'].values[0]))
        
        col5, col6, col7 = st.columns(3)
        
        with col5:
            st.metric("Fours", int(player_batting['Fours'].values[0]))
        with col6:
            st.metric("Sixes", int(player_batting['Sixes'].values[0]))
        with col7:
            st.metric("Balls Faced", int(player_batting['Balls_Faced'].values[0]))
        
        # Display detailed stats table
        st.markdown("#### Detailed Statistics")
        st.dataframe(player_batting, use_container_width=True, hide_index=True)
    else:
        st.warning("No batting statistics available for this player.")

with tab2:
    st.markdown(f"### Bowling Performance - {selected_player}")
    
    # Get bowling stats
    player_bowling = an.get_bowling_stats(deliveries_df, selected_player)
    
    if not player_bowling.empty:
        # Display metrics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Wickets", int(player_bowling['Wickets'].values[0]))
        with col2:
            st.metric("Economy", f"{player_bowling['Economy'].values[0]:.2f}")
        with col3:
            st.metric("Average", f"{player_bowling['Average'].values[0]:.2f}")
        with col4:
            st.metric("Matches", int(player_bowling['Matches'].values[0]))
        
        col5, col6 = st.columns(2)
        
        with col5:
            st.metric("Runs Conceded", int(player_bowling['Runs_Conceded'].values[0]))
        with col6:
            st.metric("Overs", f"{player_bowling['Overs'].values[0]:.1f}")
        
        # Display detailed stats table
        st.markdown("#### Detailed Statistics")
        st.dataframe(player_bowling, use_container_width=True, hide_index=True)
    else:
        st.warning("No bowling statistics available for this player.")

st.markdown("---")

# Top performers section
st.markdown("### 🌟 Top Performers")

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### Top 15 Run Scorers")
    top_batsmen = an.get_top_run_scorers(deliveries_df, 15)
    st.dataframe(top_batsmen, use_container_width=True, hide_index=True)

with col2:
    st.markdown("#### Top 15 Wicket Takers")
    top_bowlers = an.get_top_wicket_takers(deliveries_df, 15)
    st.dataframe(top_bowlers, use_container_width=True, hide_index=True)