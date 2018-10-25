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
	def __init__(name):
		self.name = name
		self.cash = 0
		self.cities = []
		self.plants = []

	def set_cash(amount):
		self.cash += amount
	def set_cities(city_name):
		self.cities.add(city_name)
	def set_plants(plant):
		if len(self.plants) == 3:
			self.plants[discard_plant()] = plant
		else:
			self.plants.add(plant)

	def discard_plant():
#		prompt asking which plant the player wants to discard

	def get_cash():
		return self.cash
	def get_cities():
		return self.cities
	def get_plants():
		return self.plants()

