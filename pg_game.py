import pg_classes as pgc
import pg_board as board

class Game:
	def __init__(self, players, colors):

		def set_city_list(colors):
			cincm = { ac:board.get_colors() for ac in colors }
			return { color:board.get_cities() for color in cincm }

		def set_players(players):
			pl_li = []
			for pl in players:
				temp_pl = pgc.Player(pl)
				temp_pl.set_cash(50)
				pl_li.append(temp_pl)
			return pl_li

		self.players = set_players(players)
		self.pls = len(players)
		self.city_list = set_city_list(colors)

	def get_cities(self):
		return self.city_list

	def get_players(self):
		return self.players