from bs4 import BeautifulSoup
import requests

#F1 Driver Stats

def GetDriverWins(person):
    html_text = requests.get('https://www.formula1.com/en/results.html/2022/drivers.html').text
    soup = BeautifulSoup(html_text, 'lxml')

    drivers = soup.tbody.find_all('tr')
    for driver in drivers:
        first_name = driver.find('span', class_='hide-for-tablet').text
        last_name = driver.find('span', class_='hide-for-mobile').text
        name = first_name + ' ' + last_name
        if name.upper() == person.upper():
            driver_link = 'https://www.formula1.com' + driver.a['href']
            html_text = requests.get(driver_link).text
            break

    soup = BeautifulSoup(html_text, 'lxml')
    races = soup.tbody.find_all('tr')
    wins = 0

    for race in races:
        race_position = race.find_all('td', class_='dark')[1].text
        if race_position == '1':
            wins += 1
    return wins

def GetDriverDNFs(person):
    html_text = requests.get('https://www.formula1.com/en/results.html/2022/drivers.html').text
    soup = BeautifulSoup(html_text, 'lxml')

    drivers = soup.tbody.find_all('tr')
    for driver in drivers:
        first_name = driver.find('span', class_='hide-for-tablet').text
        last_name = driver.find('span', class_='hide-for-mobile').text
        name = first_name + ' ' + last_name
        if name.upper() == person.upper():
            driver_link = 'https://www.formula1.com' + driver.a['href']
            html_text = requests.get(driver_link).text
            break

    soup = BeautifulSoup(html_text, 'lxml')
    races = soup.tbody.find_all('tr')
    DNFs = 0

    for race in races:
        race_position = race.find_all('td', class_='dark')[1].text
        if race_position == 'DNF':
            DNFs += 1
    print(person, 'has not finished', DNFs, 'races :(')

def GetDriverAveragePlacing(person):
    html_text = requests.get('https://www.formula1.com/en/results.html/2022/drivers.html').text
    soup = BeautifulSoup(html_text, 'lxml')

    drivers = soup.tbody.find_all('tr')
    for driver in drivers:
        first_name = driver.find('span', class_='hide-for-tablet').text
        last_name = driver.find('span', class_='hide-for-mobile').text
        name = first_name + ' ' + last_name
        if name.upper() == person.upper():
            driver_link = 'https://www.formula1.com' + driver.a['href']
            html_text = requests.get(driver_link).text
            break

    soup = BeautifulSoup(html_text, 'lxml')
    races = soup.tbody.find_all('tr')
    PlacementTotal = 0
    FinishedRaces = 0

    for race in races:
        race_position = race.find_all('td', class_='dark')[1].text
        if race_position != 'DNF':
            FinishedRaces += 1
            PlacementTotal += int(race_position)
    print('His average placing everytime he finishes a race is', round(PlacementTotal/FinishedRaces))

def GetDriverPointsAndStanding(person):
    html_text = requests.get('https://www.formula1.com/en/results.html/2022/drivers.html').text
    soup = BeautifulSoup(html_text, 'lxml')

    drivers = soup.tbody.find_all('tr')
    for driver in drivers:
        first_name = driver.find('span', class_ = 'hide-for-tablet').text
        last_name = driver.find('span', class_ = 'hide-for-mobile').text
        name = first_name + ' ' + last_name
        if name.upper() == person.upper():
            standing = driver.find('td', class_ = 'dark').text
            points = driver.find('td', class_ = 'dark bold').text
            print(person, 'WDC standing: ', standing)
            print(person, 'Points: ', points)
            return

def GetDriverHighestPlacing(person):
    if GetDriverWins(person) != 0:
        return "first"

    html_text = requests.get('https://www.formula1.com/en/results.html/2022/drivers.html').text
    soup = BeautifulSoup(html_text, 'lxml')

    drivers = soup.tbody.find_all('tr')
    for driver in drivers:
        first_name = driver.find('span', class_='hide-for-tablet').text
        last_name = driver.find('span', class_='hide-for-mobile').text
        name = first_name + ' ' + last_name
        if name.upper() == person.upper():
            driver_link = 'https://www.formula1.com' + driver.a['href']
            html_text = requests.get(driver_link).text
            break

    soup = BeautifulSoup(html_text, 'lxml')
    races = soup.tbody.find_all('tr')
    highest_placing = 20
    for race in races:
        race_position = race.find_all('td', class_='dark')[1].text
        if race_position == 'DNF':
            race_position = '21'
        if int(race_position) < highest_placing:
            highest_placing = int(race_position)

    if highest_placing == 21:
        print(person, "is yet to finish a race successfully")
    else:
        print(person, "has placed", highest_placing, "in his best race this season!")




def GetTeamWins(company):
    html_text = requests.get('https://www.formula1.com/en/results.html/2022/team.html').text
    soup = BeautifulSoup(html_text, 'lxml')

    teams = soup.tbody.find_all('tr')
    for team in teams:
        team_name = team.find('a', class_='dark bold uppercase ArchiveLink').text
        if team_name.upper() == company.upper():
            html_text = requests.get('https://www.formula1.com/en/results.html/2022/drivers.html').text
            soup = BeautifulSoup(html_text, 'lxml')
            drivers = soup.tbody.find_all('tr')
            # driver_count = 0
            team_wins = 0
            for driver in drivers:
                driver_team = driver.find('a', class_='grey semi-bold uppercase ArchiveLink').text
                if driver_team.upper() == company.upper():
                    driver_name = driver.find('span', class_='hide-for-tablet').text
                    driver_name += ' ' + driver.find('span', class_= 'hide-for-mobile').text
                    team_wins += GetDriverWins(driver_name)
            return team_wins

def GetTeamPointsAndStanding(company):
    html_text = requests.get('https://www.formula1.com/en/results.html/2022/team.html').text
    soup = BeautifulSoup(html_text, 'lxml')

    teams = soup.tbody.find_all('tr')
    for team in teams:
        team_name = team.find('a', class_='dark bold uppercase ArchiveLink').text
        if team_name.upper() == company.upper():
            team_standing = team.find('td', class_='dark').text
            team_points = team.find('td', class_="dark bold").text
            return team_standing, team_points

driver_or_team = input("Do you want to enter a driver or team, type in D or T: ")
if driver_or_team.upper() == 'D':
    driver = input('Enter driver name: ')
    GetDriverPointsAndStanding(driver)
    print(driver, 'has', GetDriverWins(driver), 'race victories!')
    GetDriverDNFs(driver)
    GetDriverAveragePlacing(driver)
    GetDriverHighestPlacing(driver)
elif driver_or_team.upper() == 'T':
    team = input('Enter team name: ')
    team_standing, team_points = GetTeamPointsAndStanding(team)
    print(team, 'is placed at', team_standing, "in the constructor's championship with", team_points, 'points')
    print(team, " has ",  GetTeamWins(team), " race wins.")
