class city(name, connections):
	def __init__(self, name, connections):
		self.name = name
		for cities in connections:
			connection.add(cities)

	def buy_city(self, player):
		for cities in self.get_available():
			