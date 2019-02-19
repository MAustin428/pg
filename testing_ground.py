# Determine the player order for this round
def order_players(players):

	def cmp_plant_cost(player_a, player_b):
		a_len = len(player_a.get_plants())
		b_len = len(player_b.get_plants())
		if player_a.get_plants()[a_len-1] < player_b.get_plants()[b_len-1]:
			return True
		else:
			return False

	pl_u = players

	for i in range(len(pl_u)):
		for j in range(i+1, len(pl_u)):
			if len(pl_u[j].get_cities()) > len(pl_u[i].get_cities()):
				temp_p = pl_u[i]
				pl_u[i] = pl_u[j]
				pl_u[j] = temp_p
			elif len(pl_u[i].get_cities()) == len(pl_u[j].get_cities()):
				if cmp_plant_cost(pl_u[i], pl_u[j]):
					temp_p = pl_u[i]
					pl_u[i] = pl_u[j]
					pl_u[j] = temp_p
	return pl_u


class Player:
	def __init__(self, name):
		self.name = name
		self.cities = []
		self.plants = []

	def set_cities(self, city_list):
		for x in city_list:
			self.cities.append(x)

	def set_plants(self, plant_list):
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

		for x in plant_list:
			self.plants.append(x)
		self.plants = order_plants(self.plants)

	def get_name(self):
		return self.name

	def get_cities(self):
		return self.cities

	def get_plants(self):
		return self.plants


pl = [Player('Mike'), Player('Tom'), Player('Amy'), Player('Wayne'), Player('Lance')]
pl[0].set_cities(['A', 'B', 'C'])
pl[1].set_cities(['C', 'D', 'E'])
pl[2].set_cities([])
pl[3].set_cities(['W', 'X', 'Y', 'Z'])
pl[4].set_cities(['Boston'])

pl[0].set_plants([2, 3, 5])
pl[1].set_plants([1, 3, 2])
pl[2].set_plants([2, 1])
pl[3].set_plants([5, 4, 2])
pl[4].set_plants([1, 9])

plr = order_players(pl)
for x in plr:
	print(x.get_name(), ': ', x.get_cities(), '   : ', x.get_plants())