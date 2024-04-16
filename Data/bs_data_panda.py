from bs4 import BeautifulSoup
import requests
import pandas as pd

years = ['1930', '1934', '1938', '1950', '1954', '1958', '1962', '1966', '1970', '1974', '1978', '1982', '1986', '1990', '1994', '1998', '2002', '2006', '2010', '2014', '2018']

def get_matches(year):
    web = f'https://en.wikipedia.org/wiki/{year}_FIFA_World_Cup'

    response = requests.get(web)
    content = response.text
    soup = BeautifulSoup(content, 'lxml')

    matches = soup.find_all('div', class_='footballbox')

    home = []
    score = []
    away = []

    for match in matches:
        home.append(match.find('th', class_='fhome').get_text())
        score.append(match.find('th', class_='fscore').get_text())
        away.append(match.find('th', class_='faway').get_text())

    dict_football = {'Home': home, 'Score': score, 'Away': away}
    df_football = pd.DataFrame(dict_football)
    df_football['year'] = year
    return df_football


def get_matches_before_worldcup2022(year):
    web = f'https://web.archive.org/web/20221115040351/https://en.wikipedia.org/wiki/{year}_FIFA_World_Cup'

    response = requests.get(web)
    content = response.text
    soup = BeautifulSoup(content, 'lxml')

    matches = soup.find_all('div', class_='footballbox')

    home = []
    score = []
    away = []

    for match in matches:
        home.append(match.find('th', class_='fhome').get_text())
        score.append(match.find('th', class_='fscore').get_text())
        away.append(match.find('th', class_='faway').get_text())

    dict_football = {'Home': home, 'Score': score, 'Away': away}
    df_football = pd.DataFrame(dict_football)
    df_football['year'] = year
    return df_football

#Historica data
fifa = [get_matches(year) for year in years]

df_fifa = pd.concat(fifa, ignore_index=True)

df_fifa.to_csv('fifa_worldcup_historical data.csv', index=False)

#Fixxture
df_fixture = get_matches_before_worldcup2022('2022')
df_fixture.to_csv('fifa_worldcup_fixture.csv', index=False)
