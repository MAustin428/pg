import pg_classes as pgc
import pg_board as board
import random

# Dijkstra's Algorithm. Needed for calculating the city purchase cost.
# Placed up here to keep it out of the way during initialization.
def dij(g):
	# Each node initializes with an arbitrarily high distance cost,
	# and is passed the the neighbors from the game board city dict.
	# When it is utilized in the algorithm, it will also point to the
	# previous node in the shortest (least-costly) path to the source.
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

	# Dijkstra's Algorithm calculates the least-costly path between
	# a source node, and every node that connects to it. I apply it
	# to every node in the list in order to find the shortest path
	# between any two cities. It is possible to reduce runtime by
	# memoizing results when calculating longer paths, but...
	path_list = {}
	for key in g: 	# for each city in the graph
		v = {}		# visited nodes (initially empty)
		uv = {}		# unvisited nodes
		p = None 	# Used for storing the previous node (initially none)
		
		# Creates a dictionary of city names and nodes for each city 
		# in the graph. If the current node is the starting node, 
		# assigns a cost of 0 to travel from the starting node to 
		# the current node, for obvious reasons
		for x in g.keys():
			n = Node(g[x])
			uv[x] = n
			if x == key:
				n.set_dist(0)

		# While there are unvisited nodes, the algorithm selects the
		# lowest-cost path to travel, adds the current node to the 
		# visited nodes, and, if the total cost to go from the starting
		# node to a new node is less than the previous total cost, updates
		# the node's dist attribute accordingly. Finally, the node is
		# removed from the unvisited nodes and staged to be added as the
		# next node's prev attribute. When all nodes have been visited,
		# the dictionary (containing city:node pairs) is itself added 
		# to a dictionary, with the key being the starting city.
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

# Manages the actual gameplay. "The Rules"				
class Game:
	def __init__(self, players, colors):
		self.board = board.Board()
		self.pls = len(players)
		# Need to validate color list length is correct for given # of players, and that colors are valid colors

		# Init. Creates a dictionary containing only the city keys that will be active in this game
		def set_city_list(colors):
			# Filters the color map down to only the colors that are active in this game
			cincm = { color: cities for color, cities in self.board.get_colors().items() if color in colors }
			# Creates a dictionary containing the city lists from the above color
			# for x, y in path.items() if x in map values, and flattens it into a list of cities
			ci_li = [ci for sublist in list(cincm.values()) for ci in sublist]
			# Filters the city map keys and values down to only the cities that are in the active colored sections
			d = self.board.get_cities().items()
			e = []
			for i in d:
				j = i[1].items()
				e.append((i[0], { x: y for x, y in j if x in ci_li }))
			ci_li = { c: path for c, path in e if c in ci_li }
			return ci_li

		# Init. Creates a dictionary of cities and the number of players in that city (initally zero)
		def set_owned_list():
			cl = self.city_list
			ol = {}
			for x in cl.keys():
				ol[x] = 0
			return ol

		# Init. Creates a new player, sets their starting cash to 50, and adds it to the player list
		def set_players(players):
			pl_li = []
			for pl in players:
				temp_pl = pgc.Player(pl, self)
				temp_pl.set_cash(50)
				pl_li.append(temp_pl)
			return pl_li

		# Init. Sets the default amount of resources available at the start of the game.
		def set_resources():
			res = self.board.get_resources()
			res['coal'] = 24
			res['oil'] = 18
			res['garbage'] = 6
			res['uranium'] = 2
			return res

		# Init. Gets the plants from the game board.
		def set_plants():
			return self.board.get_plants()

		# Init. Shuffles the deck of power plant cards, except for the first eight cards,
		# which are removed, and 13, which is placed on the top of the deck. Any
		# power plant removal will need to be added here.
		def set_deck(plants):
			deck = list(self.board.get_plants().keys())
			shuff = deck[8:]
			shuff.remove(13)
			random.shuffle(shuff)
			deck = shuff
			deck.insert(0, 13)
			return deck

		# Init. Inital values for game attributes are set
		self.players = set_players(players)
		self.city_list = set_city_list(colors)
		self.cost_list = dij(self.city_list)	# Uses Dijkstra's algorith to calculate build costs ahead of time.
		self.owned_list = set_owned_list()
		self.resources = set_resources()
		self.plants = set_plants()
		self.deck = set_deck(self.plants)
		self.market = [3, 4, 5, 6]				# Current power plant market at the game start
		self.futures = [7, 8, 9, 10]			# Futures market at the game start
		self.phase = 1							# Game starts at phase 1



	# Getters that return game-wide attributes
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
	def get_plant(self, num):
		return self.plants[num]
	def get_deck(self):
		return self.deck
	def get_market(self):
		return self.market
	def get_futures(self):
		return self.futures
	def get_phase(self):
		return self.phase

	# Prune city list down to just the cities available for purchase in the current phase
	def get_available_list(self):
		el_cities = { c: k for c, k in self.get_owned_list().items() if  k < self.phase }
		av_cities = { d: l for d, l in self.city_list.items() if d in el_cities.keys() }
		return av_cities
	
	# Looks up the cost of building between two cities (not including the cost of the city itself)
	def get_cost(self, source, target):
		return self.cost_list[source][target].get_dist()

	# Calculates the total cost of building in a city, including the phase-dependent
	# cost of building in that city
	def calc_cost(self, source, target):
		node_cost = 5 + 5 * self.get_phase()
		edge_cost = self.get_cost(source, target)
		assert self.get_cost(source, target) == self.get_cost(target, source)
		c = node_cost + edge_cost
		return c

	# Allows available resources to be updated at the start of each turn,
	# or after a player purchase
	def adjust_resource(self, res, amt):
		self.resources[res] += amt

	# Draws the top card off the deck
	def draw_card(self):
		return self.deck.pop(0)

	# Updates the list of owned cities after somebody moves into a city
	def set_owned(self, city):
		self.owned_list[city] += 1


	# Directs a round of gameplay
	def play_round(self):

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

		# Allows players to bid on available power plants 
		def auction_plants(plants, players):

			# Asks the first player which plant they want to bid on, if any
			def request_plant(plants, players_t):
				plant_in_play = ''
				print(plants, ' ')
				while players_t:
					plant_in_play = input('Choose a plant to bid on, or pass: ')
					if plant_in_play not in plants:
						pop(players_t[0])
					else:
						return plant_in_play
				return 

			def request_bids(plants, players_t):
				pip = request_plant(plants, players_t)
				players_double_t = players_t[:]
				if pip:
					while len(players_double_t) > 1 :
						current_bid = pip-1
						bid_t = input('Bid on the plant, or pass: ')
						if bid_t > current_bid:
							current_bid = bid_t
							players_double_t.append(players_double_t.pop(0))
						else:
							pop(players_double_t[0])


			player_t = players[:]
			while len(players_t) > 1 :
				request_bids(plants, players_t)

game1 = Game(['Mike', 'Tom', 'Steve'], ['Red', 'Green'])
print(game1.get_cities())

for i, x in enumerate(game1.get_players()):
	ci_li = ['Tampa', 'Houston', 'Jacksonville']
	ci_li2 = ['Birmingham', 'New Orleans', 'Miami']
	print(x.get_name(), ': $', x.get_cash())
	x.starting_city(ci_li[i])
	x.buy_city(ci_li2[i])
	print(x.get_name(), ': $', x.get_cash())
