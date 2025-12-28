"""
Match Insights and Trends Page
"""

import streamlit as st
import pandas as pd
import analysis as an
import visualizations as viz

st.set_page_config(page_title="Match Insights", page_icon="📊", layout="wide")

# Load data
@st.cache_data
def load_data():
    return an.load_data()

matches_df, deliveries_df = load_data()

if matches_df is None or deliveries_df is None:
    st.error("⚠️ Data files not found!")
    st.stop()

# ==================== MATCH INSIGHTS PAGE ====================

st.title("📊 Match Insights & Trends")

# Toss Impact Analysis
st.markdown("### 🪙 Toss Impact Analysis")
toss_impact = an.get_toss_impact(matches_df)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Matches Analyzed", toss_impact['total_matches'])
with col2:
    st.metric("Toss Winner Won Match", toss_impact['toss_winner_won_match'])
with col3:
    st.metric("Win Percentage", f"{toss_impact['win_percentage']}%")

st.info(f"📌 Teams that won the toss also won the match {toss_impact['win_percentage']}% of the time.")

st.markdown("---")

# Venue Statistics
st.markdown("### 🏟️ Venue Statistics")
venue_stats = an.get_venue_stats(matches_df)

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("#### Top 15 Most Used Venues")
    st.dataframe(venue_stats.head(15), use_container_width=True, hide_index=True)

with col2:
    st.markdown("#### Quick Stats")
    st.metric("Total Venues", len(venue_stats))
    st.metric("Most Used Venue", venue_stats.iloc[0]['Venue'])
    st.metric("Matches at Top Venue", int(venue_stats.iloc[0]['Matches_Played']))

st.markdown("---")

# Season Statistics
st.markdown("### 📅 Season-wise Match Analysis")
season_matches = an.get_matches_by_season(matches_df)

col1, col2 = st.columns(2)

with col1:
    viz.show_matches_per_season(season_matches)

with col2:
    season_df = pd.DataFrame({
        'Season': season_matches.index,
        'Matches': season_matches.values
    })
    st.dataframe(season_df, use_container_width=True, hide_index=True, height=400)

st.markdown("---")

# IPL Winners
st.markdown("### 🏆 IPL Champions History")
season_winners = an.get_season_winners(matches_df)
st.dataframe(season_winners, use_container_width=True, hide_index=True)