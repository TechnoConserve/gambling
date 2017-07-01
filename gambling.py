#! /usr/bin/python python3

from lxml import html
import requests
import teams
import players

URL = 'http://www.hockey-reference.com/teams/'

page = requests.get(URL)
tree = html.fromstring(page.content)
teamCodes = {}

def getCodes():

	for element in tree.xpath('//table[@id="active_franchises"]//a'):
		href = element.attrib['href']
		code = href[7:10]
		name = element.text_content()
		teamCodes[name] = code


def getTeams():

	teamsWeb = tree.xpath('//table[@id="active_franchises"]//a/text()')
	statsWeb = tree.xpath('//table[@id="active_franchises"]//tr[@class!="partial_table"]/td/text()')

	row = 1
	for team in teamsWeb:
		name = team
		code = teamCodes[name]
		players = getPlayers(code)
		origin = statsWeb[row]
		games = statsWeb[row + 3]
		win = statsWeb[row + 4]
		loss = statsWeb[row + 5]
		tie = statsWeb[row + 6]
		overtime = statsWeb[row + 7]
		points = statsWeb[row + 8]
		pp = statsWeb[row + 9]
		plyoff = statsWeb[row + 10]
		div = statsWeb[row + 11]
		conf = statsWeb[row + 12]
		league = statsWeb[row + 13]
		stan = statsWeb[row + 14]

		addition = teams.Team(name, code, players, origin, games, win, loss, tie, overtime, points, pp, plyoff, div, conf, league, stan)

		print("***************************************        " + name + "        ***************************************************************")
		print(addition)

		row += 16

def getPlayers(code):
	teamPage = requests.get(URL + code + '/2016.html')
	teamTree = html.fromstring(teamPage.content)

	playersWeb = teamTree.xpath('//table[@id="roster"]//a/text()')
	playerStats = teamTree.xpath('//table[@id="roster"]/tbody/tr/td/text()')

	if '\xa0' in playerStats:
		playerStats.remove('\xa0')

	teamPlayers = []

	row = 0
	for player in playersWeb:
		team = code
		name = player
		position = playerStats[row + 1]
		age = playerStats[row + 2]
		height = playerStats[row + 3]
		weight = playerStats[row + 4]
		experience = playerStats[row + 6]
		summary = playerStats[row + 8]
		salary = playerStats[row + 9]

		addition = players.Player(team, name, position, age, height, weight, experience, summary, salary)
		teamPlayers.append(addition)

		row += 10

	return teamPlayers

def getProbability(team, againstTeam, weight, stat, result):
	result = 0
	probability = 0.0
	statsToTest = [wins, losses, ties, points]

	for stat in statsToTest:
		prob = team.stat - againstTeam.stat

	return probability

def simulateMatch(team, againstTeam):

	matchPage = requests.get('http://www.hockey-reference.com/leagues/NHL_2016_games.html')
	teamTree = html.fromstring(matchPage.content)

	matchTeamsWeb = teamTree.xpath('//table[@id="games"]//a/text()')
	matchGoalsWeb = teamTree.xpath('//table[@id="games"]/tbody/tr/td/text()')

	matchTeams = []
	matchGoals = []

	for string in matchTeamsWeb:
		if '-' not in string:
			matchTeams.append(string)
	
	for string in matchGoalsWeb:
		if 'O' not in string and '-' not in string and int(string) < 17:
			matchGoals.append(string)

	wins = 0
	losses = 0
	ties = 0
	for x in range(0, len(matchGoals)):

		if x % 2 == 0 and matchTeams[x] == team and matchTeams[x + 1] == againstTeam:
			goalsFor = matchGoals[x]
			goalsAgainst = matchGoals[x + 1]

			if goalsFor > goalsAgainst:
				wins = wins + 1
			elif goalsFor < goalsAgainst:
				losses = losses + 1
			else:
				ties = ties + 1

		if x % 2 != 0 and matchTeams[x] == team and matchTeams[x - 1] == againstTeam:
			goalsFor = matchGoals[x]
			goalsAgainst = matchGoals[x - 1]

			if goalsFor > goalsAgainst:
				wins = wins + 1
			elif goalsFor < goalsAgainst:
				losses = losses + 1
			else:
				ties = ties + 1

	print(team + ' against ' + againstTeam + ':\nWins: {}, Losses: {}, Ties: {}\n'.format(wins, losses, ties))
	return ties/2 + wins - losses

