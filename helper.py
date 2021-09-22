import numpy as np


# goals ranking
def fetch_allteams(df, team):
    goals_ranking = df.sort_values(by=['Goals'], ascending=False).reset_index()
    goals_ranking.index = np.arange(1, len(df) + 1)
    goals_ranking.insert(4, 'Overall Rank', range(1, 1 + len(df)))
    goals_ranking.drop(['index', 'Shots pg',
                        'yellow_cards', 'red_cards', 'Possession%', 'Pass%', 'AerialsWon',
                        'Rating'], axis=1, inplace=True)

    if team == 'Overall':
        temp_df = goals_ranking
    if team != 'Overall':
        temp_df = goals_ranking[goals_ranking['Team'] == team]

    x = temp_df.sort_values(by=['Goals'], ascending=False)
    return x


def fetch_allteams_rating(df, club):
    club_ratings_df = df.filter(['Team', 'Rating'], axis=1)
    club_ratings_df.index = np.arange(1, len(df) + 1)
    club_ratings_df.insert(2, 'Overall Rank', range(1, 1 + len(df)))

    if club == 'Overall':
        club_df = club_ratings_df
    if club != 'Overall':
        club_df = club_ratings_df[club_ratings_df['Team'] == club]

    return club_df


def goal_ranking(df):
    goals_ranking = df.sort_values(by=['Goals'], ascending=False).reset_index()
    goals_ranking.drop(
        ['index', 'Shots pg', 'yellow_cards', 'red_cards', 'Possession%', 'Pass%', 'AerialsWon', 'Rating'], axis=1,
        inplace=True)

    return goals_ranking


def allteam_list(df):
    allteams = df['Team'].tolist()
    allteams.sort()
    allteams.insert(0, 'Overall')

    return allteams


# overall club rating graph
def overall_stats(df):
    overall_stats_df = df
    return overall_stats_df


def allteam_rating(df):
    allteams_rating = df['Team'].tolist()
    allteams_rating.sort()
    allteams_rating.insert(0, 'Overall')

    return allteams_rating


# bundelsiga
def german_rating(df):
    german_league_df = df[df['Tournament'] == 'Bundesliga'].reset_index()
    german_rating = german_league_df['Team'].tolist()
    german_rating.sort()
    german_rating.insert(0, 'Overall')

    return german_rating


def fetch_german_rating(df, germanclub):
    german_league_df = df[df['Tournament'] == 'Bundesliga'].reset_index()
    german_league_df.index = np.arange(1, len(german_league_df) + 1)
    german_league_df.drop(['index', 'Tournament', 'Shots pg', 'yellow_cards', 'red_cards',
                           'Possession%', 'Pass%', 'AerialsWon'], axis=1, inplace=True)
    if germanclub == 'Overall':
        german_club_df = german_league_df
    if germanclub != 'Overall':
        german_club_df = german_league_df[german_league_df['Team'] == germanclub]

    return german_club_df


# laliga
def spanish_rating(df):
    spanish_league_df = df[df['Tournament'] == 'LaLiga'].reset_index()

    spanish_rating = spanish_league_df['Team'].tolist()
    spanish_rating.sort()
    spanish_rating.insert(0, 'Overall')

    return spanish_rating


def fetch_spanish_rating(df, spanishclub):
    spanish_league_df = df[df['Tournament'] == 'LaLiga'].reset_index()
    spanish_league_df.index = np.arange(1, len(spanish_league_df) + 1)
    spanish_league_df.drop(['index', 'Tournament', 'Shots pg', 'yellow_cards', 'red_cards',
                            'Possession%', 'Pass%', 'AerialsWon'], axis=1, inplace=True)
    if spanishclub == 'Overall':
        spanish_club_df = spanish_league_df
    if spanishclub != 'Overall':
        spanish_club_df = spanish_league_df[spanish_league_df['Team'] == spanishclub]

    return spanish_club_df


# Ligue 1

def french_rating(df):
    french_league_df = df[df['Tournament'] == 'Ligue 1'].reset_index()

    french_rating = french_league_df['Team'].tolist()
    french_rating.sort()
    french_rating.insert(0, 'Overall')

    return french_rating


def fetch_french_rating(df, frenchclub):
    french_league_df = df[df['Tournament'] == 'Ligue 1'].reset_index()
    french_league_df.index = np.arange(1, len(french_league_df) + 1)
    french_league_df.drop(['index', 'Tournament', 'Shots pg', 'yellow_cards', 'red_cards',
                           'Possession%', 'Pass%', 'AerialsWon'], axis=1, inplace=True)
    if frenchclub == 'Overall':
        french_club_df = french_league_df
    if frenchclub != 'Overall':
        french_club_df = french_league_df[french_league_df['Team'] == frenchclub]

    return french_club_df


# EPL

def english_rating(df):
    english_league_df = df[df['Tournament'] == 'Premier League'].reset_index()

    english_rating = english_league_df['Team'].tolist()
    english_rating.sort()
    english_rating.insert(0, 'Overall')

    return english_rating


def fetch_english_rating(df, englishclub):
    english_league_df = df[df['Tournament'] == 'Premier League'].reset_index()
    english_league_df.index = np.arange(1, len(english_league_df) + 1)
    english_league_df.drop(['index', 'Tournament', 'Shots pg', 'yellow_cards', 'red_cards',
                            'Possession%', 'Pass%', 'AerialsWon'], axis=1, inplace=True)
    if englishclub == 'Overall':
        english_club_df = english_league_df
    if englishclub != 'Overall':
        english_club_df = english_league_df[english_league_df['Team'] == englishclub]

    return english_club_df


# Serie A

def italian_rating(df):
    italian_league_df = df[df['Tournament'] == 'Serie A'].reset_index()

    italian_rating = italian_league_df['Team'].tolist()
    italian_rating.sort()
    italian_rating.insert(0, 'Overall')

    return italian_rating


def fetch_italian_rating(df, italianclub):
    italian_league_df = df[df['Tournament'] == 'Serie A'].reset_index()
    italian_league_df.index = np.arange(1, len(italian_league_df) + 1)
    italian_league_df.drop(['index', 'Tournament', 'Shots pg', 'yellow_cards', 'red_cards',
                            'Possession%', 'Pass%', 'AerialsWon'], axis=1, inplace=True)
    if italianclub == 'Overall':
        italian_club_df = italian_league_df
    if italianclub != 'Overall':
        italian_club_df = italian_league_df[italian_league_df['Team'] == italianclub]

    return italian_club_df


# leagues
def leagues(df):
    leagues = df['Tournament'].unique().tolist()
    leagues.sort()
    return leagues
