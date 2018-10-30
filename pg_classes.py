class City:
	def __init__(self, name, connections, color):
		self.name = name
		self.color = color
		for cities in connections:
			self.connection.add(cities)

	def get_name():
		return self.name
	def get_color():
		return self.color
	def get_connections():
		return self.connection

class Player:
	def __init__(self, name, game):
		self.name = name
		self.game = game
		self.cash = 0
		self.cities = []
		self.plants = []
		self.resources = { 'coal': 0, 'oil': 0, 'garbage': 0, 'uranium': 0 }

	def set_cash(self, amount):
		self.cash += amount
	def set_city(self, city_name):
		self.cities.append(city_name)
	def set_plants(self, plant):
		if len(self.plants) == 3:
			self.plants[discard_plant()] = plant
		else:
			self.plants.append(plant)
	def set_resources(self, res, amt):
		self.resources[res] += amt

#	def discard_plant():
#		prompt asking which plant the player wants to discard

	def get_name(self):
		return self.name
	def get_cash(self):
		return self.cash
	def get_cities(self):
		return self.cities
	def get_plants(self):
		return self.plants()
	def get_resources(self):
		return self.resources()

	def starting_city(self, city):
		if city not in self.game.get_available_list():
			print('Invalid')
		else:
			self.set_city(city)
			self.game.set_owned(city)


	def buy_city(self, city):
		# Checks to see if city is available
		if city not in self.game.get_available_list():
			print('Invalid')
		else:
			# Calculates cheapest cost to connect
			cost = self.game.dij(self.cities[0], city)

		# Deduct the cost of the city from the players available cash
		if self.cash < cost:
			print('Invalid')
		else:
#			set_cash(-cost)
			set_city(city)
			self.game.set_owned(city)
			print(cost)