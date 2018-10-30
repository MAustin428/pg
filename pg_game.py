import pg_classes as pgc
import pg_board as board
import random

class Game:
	def __init__(self, players, colors):

		self.pls = len(players)
		# Need to validate color list length is correct for given # of players, and that colors are valid colors

		# Creates a dictionary containing only the city keys that will be active in this game
		def set_city_list(colors):
			# Filters the color map down to only the colors that are active in this game
			cincm = { color: cities for color, cities in board.get_colors().items() if color in colors }
			# Creates a dictionary containing the city lists from the above color map values, and flattens it into a list of cities
			ci_li = [ci for sublist in list(cincm.values()) for ci in sublist]
			# Filters the city map down to only the cities that are in the active colored sections
			ci_di = { c: path for c, path in board.get_cities().items() if c in  ci_li }
			return ci_di

		def set_owned_list(self):
			cl = self.city_list
			ol = {}
			for x in cl.keys():
				ol[x] = 0
			return ol

		# Creates a new player, sets their starting cash to 50, and adds it to the player list
		def set_players(players):
			pl_li = []
			for pl in players:
				temp_pl = pgc.Player(pl, self)
				temp_pl.set_cash(50)
				pl_li.append(temp_pl)
			return pl_li

		def set_resources():
			res = board.get_resources()
			res['coal'] = 24
			res['oil'] = 18
			res['garbage'] = 6
			res['uranium'] = 2
			return res

		def set_deck():
			deck = list(board.get_plants().keys())
			shuff = deck[8:]
			shuff.remove(13)
			random.shuffle(shuff)
			deck = shuff
			return deck

		def set_plants():
			return board.get_plants()

		self.players = set_players(players)
		self.city_list = set_city_list(colors)
		self.owned_list = set_owned_list(self)
		self.resources = set_resources()
		self.deck = set_deck()
		self.plants = set_plants()
		self.deck.insert(0, 13)
		self.market = [3, 4, 5, 6]
		self.futures = [7, 8, 9, 10]
		self.phase = 1			# Game starts at phase 1

	def get_players(self):
		return self.players
	def get_cities(self):
		return self.city_list
	def get_city(self, name):
		return self.city_list[name]
	def get_owned_list(self):
		return self.owned_list
	def get_resources(self):
		return self.resources
	def get_deck(self):
		return self.deck
	def get_market(self):
		return self.market
	def get_futures(self):
		return self.futures
	def get_phase(self):
		return self.phase
	def get_available_list(self):
		# Prune city list down to just the cities available for purchase in the current phase
		el_cities = { c: k for c, k in self.get_owned_list().items() if  k < self.phase }
		av_cities = { d: l for d, l in self.city_list.items() if d in el_cities.keys() }
		return av_cities
	
	def dij(self, source, target):
		s = self.get_city(source)
		return s

	def adjust_resource(self, res, amt):
		self.resources[res] += amt

	def draw_card(self):
		return self.deck.pop(0)

	def set_owned(self, city):
		self.owned_list[city] += 1

game1 = Game(['Mike', 'Tom', 'Steve'], ['Red', 'Green'])
print(game1.get_cities())
print(game1.get_deck())
print(game1.get_market(), game1.get_futures())

for i, x in enumerate(game1.get_players()):
	ci_li = ['Tampa', 'Houston', 'Jacksonville']
	ci_li2 = ['Miami', 'New Orleans', 'Birmingham']
	x.starting_city(ci_li[i])
	print(x.get_name())
	x.buy_city(ci_li2[i])