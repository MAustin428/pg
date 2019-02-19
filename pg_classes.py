class Player:
	# When the game is started, the player class is instantiated with the player name
	# and the game itself as parameters. The player has no cash, cities, plants, or
	# resources until the game assigns them during the setup phase
	def __init__(self, name, game):
		self.name = name
		self.game = game
		self.cash = 0
		self.cities = []
		self.plants = []
		self.resources = { 'coal': 0, 'oil': 0, 'garbage': 0, 'uranium': 0 }

	# Setter methods to allow changing of the player's game data
	def set_cash(self, amount):
		self.cash += amount
	def set_city(self, city_name):
		self.cities.append(city_name)
	def set_plants(self, plant):

		def order_plants(a_list):
			ps = a_list
			l = len(ps)
			for i in range(l):
				for j in range(i+1, l):
					if ps[i] > ps[j]:
						t = ps[i]
						ps[i] = a_list[j]
						ps[j] = t
			return(ps)

			
		if len(self.plants) == 3:
			# Discards the lowest-cost plantThis will eventually need 
			# to be a prompt asking the player which plant dicard.
			self.plants[0] = plant
		else:
			self.plants.append(plant)
		self.plants = order_plants(self.plants)
		for x in self.plants:
			print(x)

	def set_resources(self, res, amt):
		self.resources[res] += amt


	# Getter methods that allow other classes to view the player's game data
	def get_name(self):
		return self.name
	def get_cash(self):
		return self.cash
	def get_cities(self):
		return self.cities
	def get_plants(self):
		return self.plants
	def get_resources(self):
		return self.resources

	# Assigns the player's starting city. Only works if the player chooses an unowned
	# city in the selected color zones, and the player doesn't already own a city
	def starting_city(self, city):
		if city not in self.game.get_available_list() or self.get_cities():
			print('Invalid')
		else:
			self.set_city(city)
			self.game.set_owned(city)

	# Allows the player to buy a city
	def buy_city(self, city):
		# Checks to see if city is available. Exits the function gracefully if not
		if city not in self.game.get_available_list():
			print('Invalid')
			return None
		else:
			# Calculates cheapest cost to connect the two cities
			costs = [ self.game.calc_cost(x, city) for x in self.cities ]
			cost = min(costs)

		# Deduct the cost of the city from the players available cash
		if self.cash < cost:
			print('Invalid')
		else:
			self.set_cash(-cost)
			self.set_city(city)
			self.game.set_owned(city)

