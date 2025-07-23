
import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# Load datasets
matches_df = pd.read_csv("../data/matches_clean.csv")
team_stats = pd.read_csv("../data/team_stats.csv")
scorers_df = pd.read_csv("../data/scorers.csv")

# App Title and Sidebar
st.set_page_config(page_title="Premier League Dashboard", layout="wide")
st.title("⚽ Premier League 2023/24 Analytics Dashboard")
st.sidebar.title("Navigation")
view = st.sidebar.selectbox("Select View", ["Match Summary", "Team Stats", "Top Scorers"])

# Match Summary View
if view == "Match Summary":
    st.subheader("📅 Matchday Performance Overview")
    st.markdown("Explore goals scored per matchday and common scorelines.")

    goals_by_round = matches_df.groupby("matchday")["total_goals"].sum().reset_index()
    fig = px.line(goals_by_round, x="matchday", y="total_goals", markers=True,
                  title="Total Goals per Matchday", labels={"matchday": "Matchday", "total_goals": "Goals"})
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("### Most Common Scorelines")
    common_scoreline = matches_df["scoreline"].value_counts().head(10).reset_index()
    common_scoreline.columns = ["Scoreline", "Frequency"]
    fig2 = px.bar(common_scoreline, x="Scoreline", y="Frequency", title="Top 10 Most Common Scorelines")
    st.plotly_chart(fig2, use_container_width=True)

# Team Stats View
elif view == "Team Stats":
    st.subheader("📊 Team Performance Metrics")
    st.markdown("Analyze offensive and defensive performance of each team.")

    fig1 = px.scatter(team_stats, x="goalsFor", y="points", text="tla",
                     title="Goals Scored vs League Points",
                     labels={"goalsFor": "Goals Scored", "points": "Points"},
                     color_discrete_sequence=px.colors.sequential.Plasma)
    fig1.update_traces(textposition='top center')
    st.plotly_chart(fig1, use_container_width=True)

    fig2 = px.scatter(team_stats, x="avg_goals_scored", y="avg_goals_conceded",text='tla', 
                     title="Offense vs Defense: Avg Goals Scored vs Conceded",
                     labels={"avg_goals_scored": "Avg Goals Scored", "avg_goals_conceded": "Avg Goals Conceded"},
                     color_discrete_sequence=px.colors.sequential.Magma)
    fig2.update_traces(textposition='top center')
    st.plotly_chart(fig2, use_container_width=True)

  # Total Goals per Team - Bar Chart
    home_goals = matches_df.groupby("home_team")["home_goals"].sum()
    away_goals = matches_df.groupby("away_team")["away_goals"].sum()
    total_goals = home_goals.add(away_goals, fill_value=0).reset_index()
    total_goals.columns = ["team_name", "total_goals"]

    fig3 = px.bar(total_goals,
                  x="team_name", y="total_goals", color="total_goals",
                  text='total_goals',
                  title="Total Goals Scored by Each Team",
                  labels={"team_name": "Team", "total_goals": "Total Goals"})

    fig3.update_traces(textposition='outside')
    st.plotly_chart(fig3, use_container_width=True)


# Top Scorers View
elif view == "Top Scorers":
    st.subheader("🥇 Top Goal Scorers")
    st.markdown("List of top goal scorers in the season and their contribution.")

    top_scorers = scorers_df.sort_values("goals", ascending=False).head(10).reset_index(drop=True)
    top_scorers.index = top_scorers.index + 1
    fig = px.bar(top_scorers, x="name", y="goals", color="team",
                 title="Top 10 Scorers in 2023/24 Season",
                 labels={"name": "Player", "goals": "Goals Scored"})
    st.plotly_chart(fig, use_container_width=True)

    st.dataframe(top_scorers)

# Footer
st.markdown("---")
st.markdown("Built by Emmanuel Okonkwo · Data Science Portfolio · July 2025")
