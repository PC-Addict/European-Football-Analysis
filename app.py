import streamlit as st
import numpy as np
import preprocessor, helper
import plotly.express as px

df = preprocessor.preprocess()
epl_df = preprocessor.preprocess_epl()
france_df = preprocessor.preprocess_ligue1()
spain_df = preprocessor.preprocess_laliga()
german_df = preprocessor.preprocess_bundesliga()
italy_df = preprocessor.preprocess_sa()

# Sidebar
st.sidebar.title("Top 5 European League")
st.sidebar.image('https://www.moroccoworldnews.com/wp-content/uploads/2021/06/everything-you-need-to-know-about-uefa-euro-2020-800x500.jpg')
navbar = st.sidebar.radio(
    'Select an option',
    ('Overall Analysis', 'Player Stats', 'Club Rating', 'Goals Ranking', 'Bundesliga', 'La Liga', 'Ligue 1',
     'Premier League', 'Serie A')
)

# goal rank
if navbar == 'Goals Ranking':
    st.sidebar.header("Goals Ranking")
    allteams = helper.allteam_list(df)
    selected_club = st.sidebar.selectbox("Select Club", allteams)

    goal_ranking = helper.fetch_allteams(df, selected_club)
    if selected_club == 'Overall':
        st.title('Overall Goals Ranking')
    if selected_club != 'Overall':
        st.title("Goals by " + str(selected_club))
    st.table(goal_ranking)

# overall analysis
if navbar == 'Overall Analysis':
    League = df['Tournament'].unique().shape[0]
    Clubs = df['Team'].unique().shape[0]
    Goals = df['Goals'].sum()
    Highest_Rating = df['Rating'].max()

    Average_Shots = df["Shots pg"].mean()
    ASPG = float(round(Average_Shots, 2))

    Average_Possession = df["Possession%"].mean()
    AP = int(round(Average_Possession, 0))

    st.title('Top Statistics')

    col1, col2 = st.columns(2)
    with col1:
        st.header("League")
        st.title(League)
    with col2:
        st.header("Total Number of Clubs")
        st.title(Clubs)

    with col1:
        st.header("Total Number of Goals")
        st.title(Goals)
    with col2:
        st.header("Maximum Rating")
        st.title(Highest_Rating)

    with col1:
        st.header("Average Shots Per Game")
        st.title(ASPG)
    with col2:
        st.header("Average Possession")
        st.title(str(AP) + "%")
    st.title("Goals Per Club")
    overall_stats = helper.overall_stats(df)
    fig = px.treemap(overall_stats, path=[px.Constant('Team'), 'Team', 'Goals'], values='Goals',
                     color='Goals', hover_data=['Team'])
    st.plotly_chart(fig)

# club rating
if navbar == 'Club Rating':
    st.sidebar.header("Club Rating")
    allteams_rating = helper.allteam_rating(df)
    selected_club = st.sidebar.selectbox("Select Club", allteams_rating)

    club_ranking = helper.fetch_allteams_rating(df, selected_club)
    if selected_club == 'Overall':
        st.title('Overall Club Ranking')
    if selected_club != 'Overall':
        st.title("Rank of " + str(selected_club))
    st.table(club_ranking)

# bundesliga
if navbar == 'Bundesliga':
    st.sidebar.header("Bundesliga Clubs Rating")
    bundesliga_rating = helper.german_rating(df)
    selected_club = st.sidebar.selectbox("Select Club", bundesliga_rating)

    club_ranking = helper.fetch_german_rating(df, selected_club)
    if selected_club == 'Overall':
        st.title('Overall Bundesliga Clubs Ranking')
    if selected_club != 'Overall':
        st.title("Rank of " + str(selected_club))
    st.table(club_ranking)
# laliga
if navbar == 'La Liga':
    st.sidebar.header("La Liga Clubs Rating")
    laliga_rating = helper.spanish_rating(df)
    selected_club = st.sidebar.selectbox("Select Club", laliga_rating)

    club_ranking = helper.fetch_spanish_rating(df, selected_club)
    if selected_club == 'Overall':
        st.title('Overall La Liga Clubs Ranking')
    if selected_club != 'Overall':
        st.title("Rank of " + str(selected_club))
    st.table(club_ranking)

# ligue 1
if navbar == 'Ligue 1':
    st.sidebar.header("Ligue 1 Clubs Rating")
    ligue1_rating = helper.french_rating(df)
    selected_club = st.sidebar.selectbox("Select Club", ligue1_rating)

    club_ranking = helper.fetch_french_rating(df, selected_club)
    if selected_club == 'Overall':
        st.title('Overall Ligue 1 Clubs Ranking')
    if selected_club != 'Overall':
        st.title("Rank of " + str(selected_club))
    st.table(club_ranking)

# EPL
if navbar == 'Premier League':
    st.sidebar.header("Premier League Clubs Rating")
    epl_rating = helper.english_rating(df)
    selected_club = st.sidebar.selectbox("Select Club", epl_rating)

    club_ranking = helper.fetch_english_rating(df, selected_club)
    if selected_club == 'Overall':
        st.title('Overall Premier League Clubs Ranking')
    if selected_club != 'Overall':
        st.title("Rank of " + str(selected_club))
    st.table(club_ranking)

# serie A
if navbar == 'Serie A':
    st.sidebar.header("Serie A Clubs Rating")
    sa_rating = helper.italian_rating(df)
    selected_club = st.sidebar.selectbox("Select Club", sa_rating)

    club_ranking = helper.fetch_italian_rating(df, selected_club)
    if selected_club == 'Overall':
        st.title('Overall Serie A Clubs Ranking')
    if selected_club != 'Overall':
        st.title("Rank of " + str(selected_club))
    st.table(club_ranking)

# player stats

# epl stats
if navbar == 'Player Stats':
    leagues = helper.leagues(df)
    selected_league = st.sidebar.selectbox("Select League", leagues)
    if selected_league == 'Premier League':
        st.sidebar.header("EPL Stats")
        # max goals
        max_goals = epl_df[['player_name', 'games', 'goals', 'team_name']][epl_df.goals == epl_df.goals.max()]
        max_goals.index = np.arange(1, len(max_goals) + 1)
        max_goals_name = max_goals.at[1, 'player_name']
        max_goals_games = max_goals.at[1, 'games']
        max_goals_scored = max_goals.at[1, 'goals']
        max_goals_team = max_goals.at[1, 'team_name']

        # max assists
        max_assists = epl_df[['player_name', 'games', 'assists', 'team_name']][epl_df.assists == epl_df.assists.max()]
        max_assists.index = np.arange(1, len(max_assists) + 1)
        max_assists_name = max_assists.at[1, 'player_name']
        max_assists_games = max_assists.at[1, 'games']
        max_assists_scored = max_assists.at[1, 'assists']
        max_assists_team = max_assists.at[1, 'team_name']

        # max yellow card
        max_yc = epl_df[['player_name', 'games', 'yellow_cards', 'team_name']][
            epl_df.yellow_cards == epl_df.yellow_cards.max()]
        max_yc.index = np.arange(1, len(max_yc) + 1)
        max_yc_name = max_yc.at[1, 'player_name']
        max_yc_games = max_yc.at[1, 'games']
        max_yc_scored = max_yc.at[1, 'yellow_cards']
        max_yc_team = max_yc.at[1, 'team_name']

        # max red card
        max_rc = epl_df[['player_name', 'games', 'red_cards', 'team_name']][epl_df.red_cards == epl_df.red_cards.max()]
        max_rc.index = np.arange(1, len(max_rc) + 1)
        max_rc_name = max_rc.at[1, 'player_name']
        max_rc_games = max_rc.at[1, 'games']
        max_rc_scored = max_rc.at[1, 'red_cards']
        max_rc_team = max_rc.at[1, 'team_name']

        # max playing time
        max_time = epl_df[['player_name', 'games', 'time', 'team_name']][epl_df.time == epl_df.time.max()]
        max_time.index = np.arange(1, len(max_time) + 1)

        max_time_name1 = max_time.at[1, 'player_name']
        max_time_games1 = max_time.at[1, 'games']
        max_time_scored1 = max_time.at[1, 'time']
        max_time_team1 = max_time.at[1, 'team_name']

        max_time_name2 = max_time.at[2, 'player_name']
        max_time_games2 = max_time.at[2, 'games']
        max_time_scored2 = max_time.at[2, 'time']
        max_time_team2 = max_time.at[2, 'team_name']

        max_time_name3 = max_time.at[3, 'player_name']
        max_time_games3 = max_time.at[3, 'games']
        max_time_scored3 = max_time.at[3, 'time']
        max_time_team3 = max_time.at[3, 'team_name']

        max_time_name4 = max_time.at[4, 'player_name']
        max_time_games4 = max_time.at[4, 'games']
        max_time_scored4 = max_time.at[4, 'time']
        max_time_team4 = max_time.at[4, 'team_name']

        max_time_name5 = max_time.at[5, 'player_name']
        max_time_games5 = max_time.at[5, 'games']
        max_time_scored5 = max_time.at[5, 'time']
        max_time_team5 = max_time.at[5, 'team_name']

        max_time_name6 = max_time.at[6, 'player_name']
        max_time_games6 = max_time.at[6, 'games']
        max_time_scored6 = max_time.at[6, 'time']
        max_time_team6 = max_time.at[6, 'team_name']

        max_time_name7 = max_time.at[7, 'player_name']
        max_time_games7 = max_time.at[7, 'games']
        max_time_scored7 = max_time.at[7, 'time']
        max_time_team7 = max_time.at[7, 'team_name']

        st.title('Premier League Stats')
        fig = px.violin(epl_df, y="goals", x="games", color="team_name", box=True, points="all",
                        hover_data=['player_name'])
        st.plotly_chart(fig)
        # golas
        st.title('Most Goals')
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.header("Player")
            st.markdown(max_goals_name)
        with col2:
            st.header("Matches")
            st.markdown(max_goals_games)
        with col3:
            st.header("Goals")
            st.markdown(max_goals_scored)
        with col4:
            st.header("Club")
            st.markdown(max_goals_team)

        # assists
        st.title('Most Assists')
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.header("Player")
            st.markdown(max_assists_name)
        with col2:
            st.header("Matches")
            st.markdown(max_assists_games)
        with col3:
            st.header("Assists")
            st.markdown(max_assists_scored)
        with col4:
            st.header("Club")
            st.markdown(max_assists_team)

        # yellowcard
        st.title('Most Yellow Cards')
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.header("Player")
            st.markdown(max_yc_name)
        with col2:
            st.header("Matches")
            st.markdown(max_yc_games)
        with col3:
            st.header("Yellow Cards")
            st.markdown(max_yc_scored)
        with col4:
            st.header("Club")
            st.markdown(max_yc_team)

        # red CArd
        st.title('Most Red Cards')
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.header("Player")
            st.markdown(max_rc_name)
        with col2:
            st.header("Matches")
            st.markdown(max_rc_games)
        with col3:
            st.header("Red Cards")
            st.markdown(max_rc_scored)
        with col4:
            st.header("Club")
            st.markdown(max_rc_team)
        # playing time
        st.title('Maximum Play Time')
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.header("Player")
            st.markdown(max_time_name1)
            st.markdown(max_time_name2)
            st.markdown(max_time_name3)
            st.markdown(max_time_name4)
            st.markdown(max_time_name5)
            st.markdown(max_time_name6)
            st.markdown(max_time_name7)
        with col2:
            st.header("Matches")
            st.markdown(max_time_games1)
            st.markdown(max_time_games2)
            st.markdown(max_time_games3)
            st.markdown(max_time_games4)
            st.markdown(max_time_games5)
            st.markdown(max_time_games6)
            st.markdown(max_time_games7)
        with col3:
            st.header("Playing Time")
            st.markdown(max_time_scored1)
            st.markdown(max_time_scored2)
            st.markdown(max_time_scored3)
            st.markdown(max_time_scored4)
            st.markdown(max_time_scored5)
            st.markdown(max_time_scored6)
            st.markdown(max_time_scored7)
        with col4:
            st.header("Club")
            st.markdown(max_time_team1)
            st.markdown(max_time_team2)
            st.markdown(max_time_team3)
            st.markdown(max_time_team4)
            st.markdown(max_time_team5)
            st.markdown(max_time_team6)
            st.markdown(max_time_team7)

    # ligue 1 stats
    if selected_league == 'Ligue 1':
        st.sidebar.header("Ligue 1 Stats")
        # max goals
        max_goals = france_df[['player_name', 'games', 'goals', 'team_name']][france_df.goals == france_df.goals.max()]
        max_goals.index = np.arange(1, len(max_goals) + 1)
        max_goals_name = max_goals.at[1, 'player_name']
        max_goals_games = max_goals.at[1, 'games']
        max_goals_scored = max_goals.at[1, 'goals']
        max_goals_team = max_goals.at[1, 'team_name']

        # max assists
        max_assists = france_df[['player_name', 'games', 'assists', 'team_name']][
            france_df.assists == france_df.assists.max()]
        max_assists.index = np.arange(1, len(max_goals) + 1)
        max_assists_name = max_assists.at[1, 'player_name']
        max_assists_games = max_assists.at[1, 'games']
        max_assists_scored = max_assists.at[1, 'assists']
        max_assists_team = max_assists.at[1, 'team_name']

        # max yellow card
        max_yc = france_df[['player_name', 'games', 'yellow_cards', 'team_name']][
            france_df.yellow_cards == france_df.yellow_cards.max()]
        max_yc.index = np.arange(1, len(max_yc) + 1)
        max_yc_name = max_yc.at[1, 'player_name']
        max_yc_games = max_yc.at[1, 'games']
        max_yc_scored = max_yc.at[1, 'yellow_cards']
        max_yc_team = max_yc.at[1, 'team_name']

        # max red card
        max_rc = france_df[['player_name', 'games', 'red_cards', 'team_name']][
            france_df.red_cards == france_df.red_cards.max()]
        max_rc.index = np.arange(1, len(max_rc) + 1)
        max_rc_name = max_rc.at[1, 'player_name']
        max_rc_games = max_rc.at[1, 'games']
        max_rc_scored = max_rc.at[1, 'red_cards']
        max_rc_team = max_rc.at[1, 'team_name']

        # max playing time
        max_time = france_df[['player_name', 'games', 'time', 'team_name']][france_df.time == france_df.time.max()]
        max_time.index = np.arange(1, len(max_time) + 1)

        max_time_name1 = max_time.at[1, 'player_name']
        max_time_games1 = max_time.at[1, 'games']
        max_time_scored1 = max_time.at[1, 'time']
        max_time_team1 = max_time.at[1, 'team_name']

        max_time_name2 = max_time.at[2, 'player_name']
        max_time_games2 = max_time.at[2, 'games']
        max_time_scored2 = max_time.at[2, 'time']
        max_time_team2 = max_time.at[2, 'team_name']

        max_time_name3 = max_time.at[3, 'player_name']
        max_time_games3 = max_time.at[3, 'games']
        max_time_scored3 = max_time.at[3, 'time']
        max_time_team3 = max_time.at[3, 'team_name']

        max_time_name4 = max_time.at[4, 'player_name']
        max_time_games4 = max_time.at[4, 'games']
        max_time_scored4 = max_time.at[4, 'time']
        max_time_team4 = max_time.at[4, 'team_name']

        max_time_name5 = max_time.at[5, 'player_name']
        max_time_games5 = max_time.at[5, 'games']
        max_time_scored5 = max_time.at[5, 'time']
        max_time_team5 = max_time.at[5, 'team_name']

        max_time_name6 = max_time.at[6, 'player_name']
        max_time_games6 = max_time.at[6, 'games']
        max_time_scored6 = max_time.at[6, 'time']
        max_time_team6 = max_time.at[6, 'team_name']

        max_time_name7 = max_time.at[7, 'player_name']
        max_time_games7 = max_time.at[7, 'games']
        max_time_scored7 = max_time.at[7, 'time']
        max_time_team7 = max_time.at[7, 'team_name']

        max_time_name8 = max_time.at[8, 'player_name']
        max_time_games8 = max_time.at[8, 'games']
        max_time_scored8 = max_time.at[8, 'time']
        max_time_team8 = max_time.at[8, 'team_name']

        st.title('Ligue 1 Stats')
        fig = px.violin(france_df, y="goals", x="games", color="team_name", box=True, points="all",
                        hover_data=['player_name'])
        st.plotly_chart(fig)
        # golas
        st.title('Most Goals')
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.header("Player")
            st.markdown(max_goals_name)
        with col2:
            st.header("Matches")
            st.markdown(max_goals_games)
        with col3:
            st.header("Goals")
            st.markdown(max_goals_scored)
        with col4:
            st.header("Club")
            st.markdown(max_goals_team)

        # assists
        st.title('Most Assists')
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.header("Player")
            st.markdown(max_assists_name)
        with col2:
            st.header("Matches")
            st.markdown(max_assists_games)
        with col3:
            st.header("Assists")
            st.markdown(max_assists_scored)
        with col4:
            st.header("Club")
            st.markdown(max_assists_team)

        # yellowcard
        st.title('Most Yellow Cards')
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.header("Player")
            st.markdown(max_yc_name)
        with col2:
            st.header("Matches")
            st.markdown(max_yc_games)
        with col3:
            st.header("Yellow Cards")
            st.markdown(max_yc_scored)
        with col4:
            st.header("Club")
            st.markdown(max_yc_team)

        # red CArd
        st.title('Most Red Cards')
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.header("Player")
            st.markdown(max_rc_name)
        with col2:
            st.header("Matches")
            st.markdown(max_rc_games)
        with col3:
            st.header("Red Cards")
            st.markdown(max_rc_scored)
        with col4:
            st.header("Club")
            st.markdown(max_rc_team)

        # playing time
        st.title('Maximum Play Time')
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.header("Player")
            st.markdown(max_time_name1)
            st.markdown(max_time_name2)
            st.markdown(max_time_name3)
            st.markdown(max_time_name4)
            st.markdown(max_time_name5)
            st.markdown(max_time_name6)
            st.markdown(max_time_name7)
            st.markdown(max_time_name8)
        with col2:
            st.header("Matches")
            st.markdown(max_time_games1)
            st.markdown(max_time_games2)
            st.markdown(max_time_games3)
            st.markdown(max_time_games4)
            st.markdown(max_time_games5)
            st.markdown(max_time_games6)
            st.markdown(max_time_games7)
            st.markdown(max_time_games8)
        with col3:
            st.header("Playing Time")
            st.markdown(max_time_scored1)
            st.markdown(max_time_scored2)
            st.markdown(max_time_scored3)
            st.markdown(max_time_scored4)
            st.markdown(max_time_scored5)
            st.markdown(max_time_scored6)
            st.markdown(max_time_scored7)
            st.markdown(max_time_scored8)
        with col4:
            st.header("Club")
            st.markdown(max_time_team1)
            st.markdown(max_time_team2)
            st.markdown(max_time_team3)
            st.markdown(max_time_team4)
            st.markdown(max_time_team5)
            st.markdown(max_time_team6)
            st.markdown(max_time_team7)
            st.markdown(max_time_team8)

    # la liga

    if selected_league == 'LaLiga':
        st.sidebar.header("La Liga Stats")
        # max goals
        max_goals = spain_df[['player_name', 'games', 'goals', 'team_name']][spain_df.goals == spain_df.goals.max()]
        max_goals.index = np.arange(1, len(max_goals) + 1)
        max_goals_name = max_goals.at[1, 'player_name']
        max_goals_games = max_goals.at[1, 'games']
        max_goals_scored = max_goals.at[1, 'goals']
        max_goals_team = max_goals.at[1, 'team_name']

        # max assists
        max_assists = spain_df[['player_name', 'games', 'assists', 'team_name']][
            spain_df.assists == spain_df.assists.max()]
        max_assists.index = np.arange(1, len(max_goals) + 1)
        max_assists_name = max_assists.at[1, 'player_name']
        max_assists_games = max_assists.at[1, 'games']
        max_assists_scored = max_assists.at[1, 'assists']
        max_assists_team = max_assists.at[1, 'team_name']

        # max yellow card
        max_yc = spain_df[['player_name', 'games', 'yellow_cards', 'team_name']][
            spain_df.yellow_cards == spain_df.yellow_cards.max()]
        max_yc.index = np.arange(1, len(max_yc) + 1)
        max_yc_name = max_yc.at[1, 'player_name']
        max_yc_games = max_yc.at[1, 'games']
        max_yc_scored = max_yc.at[1, 'yellow_cards']
        max_yc_team = max_yc.at[1, 'team_name']

        # max red card
        max_rc = spain_df[['player_name', 'games', 'red_cards', 'team_name']][
            spain_df.red_cards == spain_df.red_cards.max()]
        max_rc.index = np.arange(1, len(max_rc) + 1)

        max_rc_name4 = max_rc.at[4, 'player_name']
        max_rc_games4 = max_rc.at[4, 'games']
        max_rc_scored4 = max_rc.at[4, 'red_cards']
        max_rc_team4 = max_rc.at[4, 'team_name']

        # max playing time
        max_time = spain_df[['player_name', 'games', 'time', 'team_name']][spain_df.time == spain_df.time.max()]
        max_time.index = np.arange(1, len(max_time) + 1)

        max_time_name1 = max_time.at[1, 'player_name']
        max_time_games1 = max_time.at[1, 'games']
        max_time_scored1 = max_time.at[1, 'time']
        max_time_team1 = max_time.at[1, 'team_name']

        max_time_name2 = max_time.at[2, 'player_name']
        max_time_games2 = max_time.at[2, 'games']
        max_time_scored2 = max_time.at[2, 'time']
        max_time_team2 = max_time.at[2, 'team_name']

        max_time_name3 = max_time.at[3, 'player_name']
        max_time_games3 = max_time.at[3, 'games']
        max_time_scored3 = max_time.at[3, 'time']
        max_time_team3 = max_time.at[3, 'team_name']

        st.title('La Liga Stats')
        fig = px.violin(spain_df, y="goals", x="games", color="team_name", box=True, points="all",
                        hover_data=['player_name'])
        st.plotly_chart(fig)
        # golas
        st.title('Most Goals')
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.header("Player")
            st.markdown(max_goals_name)
        with col2:
            st.header("Matches")
            st.markdown(max_goals_games)
        with col3:
            st.header("Goals")
            st.markdown(max_goals_scored)
        with col4:
            st.header("Club")
            st.markdown(max_goals_team)

        # assists
        st.title('Most Assists')
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.header("Player")
            st.markdown(max_assists_name)
        with col2:
            st.header("Matches")
            st.markdown(max_assists_games)
        with col3:
            st.header("Assists")
            st.markdown(max_assists_scored)
        with col4:
            st.header("Club")
            st.markdown(max_assists_team)

        # yellowcard
        st.title('Most Yellow Cards')
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.header("Player")
            st.markdown(max_yc_name)
        with col2:
            st.header("Matches")
            st.markdown(max_yc_games)
        with col3:
            st.header("Yellow Cards")
            st.markdown(max_yc_scored)
        with col4:
            st.header("Club")
            st.markdown(max_yc_team)

        # red CArd
        st.title('Most Red Cards')
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.header("Player")
            st.markdown(max_rc_name4)

        with col2:
            st.header("Matches")
            st.markdown(max_rc_games4)

        with col3:
            st.header("Red Cards")
            st.markdown(max_rc_scored4)

        with col4:
            st.header("Club")
            st.markdown(max_rc_team4)

        # playing time
        st.title('Maximum Play Time')
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.header("Player")
            st.markdown(max_time_name1)
            st.markdown(max_time_name2)
            st.markdown(max_time_name3)

        with col2:
            st.header("Matches")
            st.markdown(max_time_games1)
            st.markdown(max_time_games2)
            st.markdown(max_time_games3)

        with col3:
            st.header("Playing Time")
            st.markdown(max_time_scored1)
            st.markdown(max_time_scored2)
            st.markdown(max_time_scored3)

        with col4:
            st.header("Club")
            st.markdown(max_time_team1)
            st.markdown(max_time_team2)
            st.markdown(max_time_team3)

    # Bundesliga
    if selected_league == 'Bundesliga':
        st.sidebar.header("Bundesliga Stats")
        # max goals
        max_goals = german_df[['player_name', 'games', 'goals', 'team_name']][german_df.goals == german_df.goals.max()]
        max_goals.index = np.arange(1, len(max_goals) + 1)
        max_goals_name = max_goals.at[1, 'player_name']
        max_goals_games = max_goals.at[1, 'games']
        max_goals_scored = max_goals.at[1, 'goals']
        max_goals_team = max_goals.at[1, 'team_name']

        # max assists
        max_assists = german_df[['player_name', 'games', 'assists', 'team_name']][
            german_df.assists == german_df.assists.max()]
        max_assists.index = np.arange(1, len(max_goals) + 1)
        max_assists_name = max_assists.at[1, 'player_name']
        max_assists_games = max_assists.at[1, 'games']
        max_assists_scored = max_assists.at[1, 'assists']
        max_assists_team = max_assists.at[1, 'team_name']

        # max yellow card
        max_yc = german_df[['player_name', 'games', 'yellow_cards', 'team_name']][
            german_df.yellow_cards == german_df.yellow_cards.max()]
        max_yc.index = np.arange(1, len(max_yc) + 1)
        max_yc_name = max_yc.at[1, 'player_name']
        max_yc_games = max_yc.at[1, 'games']
        max_yc_scored = max_yc.at[1, 'yellow_cards']
        max_yc_team = max_yc.at[1, 'team_name']

        # max red card
        max_rc = german_df[['player_name', 'games', 'red_cards', 'team_name']][
            german_df.red_cards == german_df.red_cards.max()]
        max_rc.index = np.arange(1, len(max_rc) + 1)

        max_rc_name1 = max_rc.at[3, 'player_name']
        max_rc_games1 = max_rc.at[3, 'games']
        max_rc_scored1 = max_rc.at[3, 'red_cards']
        max_rc_team1 = max_rc.at[3, 'team_name']

        max_rc_name2 = max_rc.at[29, 'player_name']
        max_rc_games2 = max_rc.at[29, 'games']
        max_rc_scored2 = max_rc.at[29, 'red_cards']
        max_rc_team2 = max_rc.at[29, 'team_name']

        # max playing time
        max_time = german_df[['player_name', 'games', 'time', 'team_name']][german_df.time == german_df.time.max()]
        max_time.index = np.arange(1, len(max_time) + 1)

        max_time_name1 = max_time.at[1, 'player_name']
        max_time_games1 = max_time.at[1, 'games']
        max_time_scored1 = max_time.at[1, 'time']
        max_time_team1 = max_time.at[1, 'team_name']

        max_time_name2 = max_time.at[2, 'player_name']
        max_time_games2 = max_time.at[2, 'games']
        max_time_scored2 = max_time.at[2, 'time']
        max_time_team2 = max_time.at[2, 'team_name']

        max_time_name3 = max_time.at[3, 'player_name']
        max_time_games3 = max_time.at[3, 'games']
        max_time_scored3 = max_time.at[3, 'time']
        max_time_team3 = max_time.at[3, 'team_name']

        max_time_name4 = max_time.at[4, 'player_name']
        max_time_games4 = max_time.at[4, 'games']
        max_time_scored4 = max_time.at[4, 'time']
        max_time_team4 = max_time.at[4, 'team_name']

        max_time_name5 = max_time.at[5, 'player_name']
        max_time_games5 = max_time.at[5, 'games']
        max_time_scored5 = max_time.at[5, 'time']
        max_time_team5 = max_time.at[5, 'team_name']

        max_time_name6 = max_time.at[6, 'player_name']
        max_time_games6 = max_time.at[6, 'games']
        max_time_scored6 = max_time.at[6, 'time']
        max_time_team6 = max_time.at[6, 'team_name']

        st.title('Bundesliga Stats')
        fig = px.violin(german_df, y="goals", x="games", color="team_name", box=True, points="all",
                        hover_data=['player_name'])
        st.plotly_chart(fig)

        # golas
        st.title('Most Goals')
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.header("Player")
            st.markdown(max_goals_name)
        with col2:
            st.header("Matches")
            st.markdown(max_goals_games)
        with col3:
            st.header("Goals")
            st.markdown(max_goals_scored)
        with col4:
            st.header("Club")
            st.markdown(max_goals_team)

        # assists
        st.title('Most Assists')
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.header("Player")
            st.markdown(max_assists_name)
        with col2:
            st.header("Matches")
            st.markdown(max_assists_games)
        with col3:
            st.header("Assists")
            st.markdown(max_assists_scored)
        with col4:
            st.header("Club")
            st.markdown(max_assists_team)

        # yellowcard
        st.title('Most Yellow Cards')
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.header("Player")
            st.markdown(max_yc_name)
        with col2:
            st.header("Matches")
            st.markdown(max_yc_games)
        with col3:
            st.header("Yellow Cards")
            st.markdown(max_yc_scored)
        with col4:
            st.header("Club")
            st.markdown(max_yc_team)

        # red CArd
        st.title('Most Red Cards')
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.header("Player")
            st.markdown(max_rc_name1)
            st.markdown(max_rc_name2)
        with col2:
            st.header("Matches")
            st.markdown(max_rc_games1)
            st.markdown(max_rc_games2)
        with col3:
            st.header("Red Cards")
            st.markdown(max_rc_scored1)
            st.markdown(max_rc_scored2)
        with col4:
            st.header("Club")
            st.markdown(max_rc_team1)
            st.markdown(max_rc_team2)

        # playing time
        st.title('Maximum Play Time')
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.header("Player")
            st.markdown(max_time_name1)
            st.markdown(max_time_name2)
            st.markdown(max_time_name3)
            st.markdown(max_time_name4)
            st.markdown(max_time_name5)
            st.markdown(max_time_name6)

        with col2:
            st.header("Matches")
            st.markdown(max_time_games1)
            st.markdown(max_time_games2)
            st.markdown(max_time_games3)
            st.markdown(max_time_games4)
            st.markdown(max_time_games5)
            st.markdown(max_time_games6)

        with col3:
            st.header("Playing Time")
            st.markdown(max_time_scored1)
            st.markdown(max_time_scored2)
            st.markdown(max_time_scored3)
            st.markdown(max_time_scored4)
            st.markdown(max_time_scored5)
            st.markdown(max_time_scored6)

        with col4:
            st.header("Club")
            st.markdown(max_time_team1)
            st.markdown(max_time_team2)
            st.markdown(max_time_team3)
            st.markdown(max_time_team4)
            st.markdown(max_time_team5)
            st.markdown(max_time_team6)

    # serie A

    if selected_league == 'Serie A':
        st.sidebar.header("Serie A Stats")
        # max goals
        max_goals = italy_df[['player_name', 'games', 'goals', 'team_name']][italy_df.goals == italy_df.goals.max()]
        max_goals.index = np.arange(1, len(max_goals) + 1)
        max_goals_name = max_goals.at[1, 'player_name']
        max_goals_games = max_goals.at[1, 'games']
        max_goals_scored = max_goals.at[1, 'goals']
        max_goals_team = max_goals.at[1, 'team_name']

        # max assists
        max_assists = italy_df[['player_name', 'games', 'assists', 'team_name']][
            italy_df.assists == italy_df.assists.max()]
        max_assists.index = np.arange(1, len(max_goals) + 1)
        max_assists_name = max_assists.at[1, 'player_name']
        max_assists_games = max_assists.at[1, 'games']
        max_assists_scored = max_assists.at[1, 'assists']
        max_assists_team = max_assists.at[1, 'team_name']

        # max yellow card
        max_yc = italy_df[['player_name', 'games', 'yellow_cards', 'team_name']][
            italy_df.yellow_cards == italy_df.yellow_cards.max()]
        max_yc.index = np.arange(1, len(max_yc) + 1)
        max_yc_name = max_yc.at[1, 'player_name']
        max_yc_games = max_yc.at[1, 'games']
        max_yc_scored = max_yc.at[1, 'yellow_cards']
        max_yc_team = max_yc.at[1, 'team_name']

        # max red card
        max_rc = italy_df[['player_name', 'games', 'red_cards', 'team_name']][
            italy_df.red_cards == german_df.red_cards.max()]
        max_rc.index = np.arange(1, len(max_rc) + 1)

        max_rc_name = max_rc.at[2, 'player_name']
        max_rc_games = max_rc.at[2, 'games']
        max_rc_scored = max_rc.at[2, 'red_cards']
        max_rc_team = max_rc.at[2, 'team_name']

        # max playing time
        max_time = italy_df[['player_name', 'games', 'time', 'team_name']][italy_df.time == italy_df.time.max()]
        max_time.index = np.arange(1, len(max_time) + 1)

        max_time_name1 = max_time.at[1, 'player_name']
        max_time_games1 = max_time.at[1, 'games']
        max_time_scored1 = max_time.at[1, 'time']
        max_time_team1 = max_time.at[1, 'team_name']

        max_time_name2 = max_time.at[2, 'player_name']
        max_time_games2 = max_time.at[2, 'games']
        max_time_scored2 = max_time.at[2, 'time']
        max_time_team2 = max_time.at[2, 'team_name']

        max_time_name3 = max_time.at[3, 'player_name']
        max_time_games3 = max_time.at[3, 'games']
        max_time_scored3 = max_time.at[3, 'time']
        max_time_team3 = max_time.at[3, 'team_name']

        max_time_name4 = max_time.at[4, 'player_name']
        max_time_games4 = max_time.at[4, 'games']
        max_time_scored4 = max_time.at[4, 'time']
        max_time_team4 = max_time.at[4, 'team_name']

        st.title('Serie A Stats')
        fig = px.violin(italy_df, y="goals", x="games", color="team_name", box=True, points="all",
                        hover_data=['player_name'])
        st.plotly_chart(fig)
        # golas
        st.title('Most Goals')
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.header("Player")
            st.markdown(max_goals_name)
        with col2:
            st.header("Matches")
            st.markdown(max_goals_games)
        with col3:
            st.header("Goals")
            st.markdown(max_goals_scored)
        with col4:
            st.header("Club")
            st.markdown(max_goals_team)

        # assists
        st.title('Most Assists')
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.header("Player")
            st.markdown(max_assists_name)
        with col2:
            st.header("Matches")
            st.markdown(max_assists_games)
        with col3:
            st.header("Assists")
            st.markdown(max_assists_scored)
        with col4:
            st.header("Club")
            st.markdown(max_assists_team)

        # yellowcard
        st.title('Most Yellow Cards')
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.header("Player")
            st.markdown(max_yc_name)
        with col2:
            st.header("Matches")
            st.markdown(max_yc_games)
        with col3:
            st.header("Yellow Cards")
            st.markdown(max_yc_scored)
        with col4:
            st.header("Club")
            st.markdown(max_yc_team)

        # red CArd
        st.title('Most Red Cards')
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.header("Player")
            st.markdown(max_rc_name)
        with col2:
            st.header("Matches")
            st.markdown(max_rc_games)
        with col3:
            st.header("Red Cards")
            st.markdown(max_rc_scored)
        with col4:
            st.header("Club")
            st.markdown(max_rc_team)

        # playing time
        st.title('Maximum Play Time')
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.header("Player")
            st.markdown(max_time_name1)
            st.markdown(max_time_name2)
            st.markdown(max_time_name3)
            st.markdown(max_time_name4)

        with col2:
            st.header("Matches")
            st.markdown(max_time_games1)
            st.markdown(max_time_games2)
            st.markdown(max_time_games3)
            st.markdown(max_time_games4)

        with col3:
            st.header("Playing Time")
            st.markdown(max_time_scored1)
            st.markdown(max_time_scored2)
            st.markdown(max_time_scored3)
            st.markdown(max_time_scored4)

        with col4:
            st.header("Club")
            st.markdown(max_time_team1)
            st.markdown(max_time_team2)
            st.markdown(max_time_team3)
            st.markdown(max_time_team4)
