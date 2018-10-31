import pg_classes as pgc
import pg_board as board
import random

def dij(g):
	class Node:
		def __init__(self, neighbors):
			self.dist = 0xffffffff
			self.neighbors = neighbors

		def set_prev(self, node):
			self.prev = node
		def set_dist(self, dist):
			self.dist = dist

		def get_prev(self):
			return self.prev
		def get_dist(self):
			return self.dist
		def get_neighbors(self):
			return self.neighbors

	path_list = {}
	for key in g:
		v = {}
		uv = {}
		d = 0
		p = None 
		for x in g.keys():
			n = Node(g[x])
			uv[x] = n
			if x == key:
				n.set_dist(0)

		while uv:
			act = min(uv, key=lambda x: uv[x].get_dist())
			uv[act].set_prev(p)
			v[act] = uv[act]
			for y in uv[act].get_neighbors() :
				if y not in v:
					trial_dist = uv[act].get_dist() + uv[act].get_neighbors()[y]
					if uv[y].get_dist() > trial_dist:
						uv[y].set_dist(trial_dist)
			p = uv.pop(act)
		path_list[key] = v
	return path_list

				
class Game:
	def __init__(self, players, colors):

		self.pls = len(players)
		# Need to validate color list length is correct for given # of players, and that colors are valid colors

		# Creates a dictionary containing only the city keys that will be active in this game
		def set_city_list(colors):
			# Filters the color map down to only the colors that are active in this game
			cincm = { color: cities for color, cities in board.get_colors().items() if color in colors }
			# Creates a dictionary containing the city lists from the above colorfor x, y in path.items() if x in map values, and flattens it into a list of cities
			ci_li = [ci for sublist in list(cincm.values()) for ci in sublist]
			# Filters the city map keys and values down to only the cities that are in the active colored sections
			d = board.get_cities().items()
			e = []
			for i in d:
				j = i[1].items()
				e.append((i[0], { x: y for x, y in j if x in ci_li }))
			ci_li = { c: path for c, path in e if c in ci_li }
			return ci_li

		def set_owned_list():
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
		self.cost_list = dij(self.city_list)
		self.owned_list = set_owned_list()
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
	def get_cost(self, source, target):
		return self.cost_list[source][target].get_dist()

	def calc_cost(self, source, target):
		node_cost = 5 + 5 * self.get_phase()
		edge_cost = self.get_cost(source, target)
		assert self.get_cost(source, target) == self.get_cost(target, source)
		c = node_cost + edge_cost
		return c

	def adjust_resource(self, res, amt):
		self.resources[res] += amt

	def draw_card(self):
		return self.deck.pop(0)

	def set_owned(self, city):
		self.owned_list[city] += 1

#game1 = Game(['Mike', 'Tom', 'Steve'], ['Red', 'Green'])
#print(game1.get_cities())

#for i, x in enumerate(game1.get_players()):
#	ci_li = ['Tampa', 'Houston', 'Jacksonville']
#	ci_li2 = ['Birmingham', 'New Orleans', 'Miami']
#	print(x.get_name(), ': $', x.get_cash())
#	x.starting_city(ci_li[i])
#	x.buy_city(ci_li2[i])
#	print(x.get_name(), ': $', x.get_cash())
