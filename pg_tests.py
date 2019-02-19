def order_test(self, l):
	for i, x in enumerate(l):
		next_x = l[i+1]
		assert len(x.get_cities()) >= len(next_x.get_cities())
		if len(x.get_cities()) == len(next_x.get_cities()):
			assert cmp_plant_cost()

def test_nodes(self):
	for x in self.city_map:
		for y in self.city_map[x]:
			assert y in city_map, 'City not found; check spelling %r %r' %x %y.keys()
			assert (self.city_map[x][y]) == self.city_map[y][x], 'City is missing bidirectional path %r %r' %x %y[0]
		in_color = False
		for color in self.color_map:
			assert len(self.color_map[color]) == 7, 'Cities not zoned into colored regions correctly'
			if x in self.color_map[color]:
				assert in_color == False, 'Duplicate city %r' %x
				in_color = True
		assert in_color == True, 'City missing %r' %x

def test_plants(self):
	for x in self.power_plants:
		assert len(self.power_plants[x]) == 3, 'Power plant lacking required information: %r' %x[0]
	assert len(self.power_plants) == 42, 'Power plant missing from list'
