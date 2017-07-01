class Player:
	playerList = [] # list of all player objects

	def __init__(self, team, name, pos, age, ht, wt, exp, summ, sal):
		self.team = team
		self.name = name
		self.position = pos
		self.age = age
		self.height = ht
		self.weight = wt
		self.experience = exp # Number of years experience prior to current season
		self.summary = summ # Summary of stats which varies in format based on position
		self.salary = sal
		self.playerList.append(self)

	def __str__(self):
		return "Name: {}\nTeam: {}\nPosition: {}\nAge: {}\nHeight: {}\nWeight: {}\nExperience: {}\nSummary: {}\nSalary: {}\n\n".format(self.name, self.team, self.position, self.age, self.height, self.weight, self.experience, self.summary, self.salary)

	def __repr__(self):
		return "Name: {}\nTeam: {}\nPosition: {}\nAge: {}\nHeight: {}\nWeight: {}\nExperience: {}\nSummary: {}\nSalary: {}\n\n".format(self.name, self.team, self.position, self.age, self.height, self.weight, self.experience, self.summary, self.salary)