class Team:
	tList = [] # list of all team objects

	def __init__(self, name, code, players, origin, games, win, loss, tie, overtime, points, pp, plyoff, div, conf, league, stan):
		self.name = name
		self.code = code
		self.players = players
		self.originYear = origin
		self.gamesPlayed = games
		self.wins = win
		self.losses = loss
		self.ties = tie
		self.overtimeLoss = overtime
		self.points = points
		self.pointsPercent = pp
		self.numPlyof = plyoff
		self.div = div
		self.conf = conf
		self.lChamp = league
		self.stan = stan
		self.tList.append(self)

	def __str__(self):
		return "Name: {}\nCode: {}\nOrigin Year: {}\nGames Played: {}\nWins: {}\nLosses: {}\nTies: {}\nOvertime Losses: {}\nPoints: {}\nPoints Percentage: {}\nPlayoff Appearances: {}\nTimes First (or tied) in Division: {}\nConferance Championships: {}\nLeague Championships: {}\nStanley Cup Wins: {}\n\nPlayers: {}".format(self.name, self.code, self.originYear, self.gamesPlayed, self.wins, self.losses, self.ties, self.overtimeLoss, self.points, self.pointsPercent, self.numPlyof, self.div, self.conf, self.lChamp, self.stan, self.players)