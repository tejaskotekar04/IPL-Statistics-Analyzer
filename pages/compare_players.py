"""
Player Comparison Page
"""

import streamlit as st
import analysis as an
import visualizations as viz

st.set_page_config(page_title="Compare Players", page_icon="⚖️", layout="wide")

# Load data
@st.cache_data
def load_data():
    return an.load_data()

matches_df, deliveries_df = load_data()

if matches_df is None or deliveries_df is None:
    st.error("⚠️ Data files not found!")
    st.stop()

# ==================== COMPARE PLAYERS PAGE ====================

st.title("⚖️ Compare Players")

# Get all players
all_players = an.get_all_players(deliveries_df)

st.markdown("### Select players to compare (Choose 2-5 players)")

# Multi-select for players
selected_players = st.multiselect(
    "Select Players",
    all_players,
    default=[]
)

if len(selected_players) < 2:
    st.warning("⚠️ Please select at least 2 players to compare.")
elif len(selected_players) > 5:
    st.warning("⚠️ Please select maximum 5 players for better visualization.")
else:
    st.markdown("---")
    
    # Batting Comparison
    st.markdown("### 🏏 Batting Comparison")
    
    # Get batting stats for all players
    all_batting_stats = an.get_batting_stats(deliveries_df)
    
    # Filter for selected players
    comparison_data = all_batting_stats[all_batting_stats['Player'].isin(selected_players)]
    
    if not comparison_data.empty:
        # Display comparison table
        st.dataframe(comparison_data, use_container_width=True, hide_index=True)
        
        # Comparison charts
        st.markdown("### 📊 Visual Comparison")
        viz.show_player_comparison(comparison_data)
    
    st.markdown("---")
    
    # Bowling Comparison
    st.markdown("### ⚾ Bowling Comparison")
    
    # Get bowling stats for all players
    all_bowling_stats = an.get_bowling_stats(deliveries_df)
    
    # Filter for selected players
    bowling_comparison = all_bowling_stats[all_bowling_stats['Player'].isin(selected_players)]
    
    if not bowling_comparison.empty:
        st.dataframe(bowling_comparison, use_container_width=True, hide_index=True)
    else:
        st.info("No bowling statistics available for the selected players.")