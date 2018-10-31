import time

city_map = {
			'Seattle': {'Billings': 9, 'Boise': 12, 'Portland': 3},
			'Portland': {'Seattle': 3, 'Boise': 13, 'San Francisco': 24},
			'San Francisco': {'Portland': 24, 'Boise': 23, 'Salt Lake City': 27, 'Las Vegas': 14, 'Los Angeles': 9},
			'Los Angeles': {'San Francisco': 9, 'Las Vegas': 9, 'San Diego': 3},
			'San Diego': {'Los Angeles': 3, 'Las Vegas': 9, 'Phoenix': 14},
			'Boise': {'Billings': 12, 'Cheyenne': 24, 'Salt Lake City': 8, 'San Francisco': 23, 'Portland': 13, 'Seattle': 12},
			'Salt Lake City': {'Denver': 21, 'Santa Fe': 28, 'Las Vegas': 18, 'San Francisco': 27, 'Boise': 8},
			'Las Vegas': {'Salt Lake City': 18, 'Santa Fe': 27, 'Phoenix': 15, 'San Diego': 9, 'Los Angeles': 9, 'San Francisco': 14},
			'Phoenix': {'Santa Fe': 18, 'San Diego': 14, 'Las Vegas': 15},
			'Billings': {'Fargo': 17, 'Minneapolis': 18, 'Cheyenne': 9, 'Boise': 12, 'Seattle': 9},
			'Cheyenne': {'Minneapolis': 18, 'Omaha': 14, 'Denver': 0, 'Boise': 24, 'Billings': 9},
			'Denver': {'Cheyenne': 0, 'Kansas City': 16, 'Santa Fe': 13, 'Salt Lake City': 21},
			'Santa Fe': {'Denver': 13, 'Kansas City': 16, 'Oklahoma City': 15, 'Dallas': 16, 'Houston': 21, 'Phoenix': 18, 'Las Vegas': 27, 'Salt Lake City': 28},
			'Fargo': {'Duluth': 6, 'Minneapolis': 6, 'Billings': 17},
			'Duluth': {'Detroit': 15, 'Chicago': 12, 'Minneapolis': 5, 'Fargo': 6},
			'Minneapolis': {'Duluth': 5, 'Chicago': 8, 'Omaha': 8, 'Cheyenne': 18, 'Billings': 18, 'Fargo': 6},
			'Omaha': {'Minneapolis': 8, 'Chicago': 13, 'Kansas City': 5, 'Cheyenne': 14},
			'Kansas City': {'Chicago': 8, 'St Louis': 6, 'Memphis': 12, 'Oklahoma City': 8, 'Santa Fe': 16, 'Denver': 16, 'Omaha': 5},
			'Oklahoma City': {'Kansas City': 8, 'Memphis': 14, 'Dallas': 3, 'Santa Fe': 15},
			'Dallas': {'Memphis': 12, 'New Orleans': 12, 'Houston': 5, 'Santa Fe': 16, 'Oklahoma City': 3},
			'Houston': {'New Orleans': 8, 'Santa Fe': 21, 'Dallas': 5},
			'Chicago': {'Detroit': 7, 'Cincinnati': 7, 'St Louis': 10, 'Kansas City': 8, 'Omaha': 13, 'Minneapolis': 8, 'Duluth': 12},
			'St Louis': {'Chicago': 10, 'Cincinnati': 12, 'Atlanta': 12, 'Memphis': 7, 'Kansas City': 6},
			'Memphis': {'St Louis': 7, 'Birmingham': 6, 'New Orleans': 7, 'Dallas': 12, 'Oklahoma City': 14, 'Kansas City': 12},
			'New Orleans': {'Memphis': 7, 'Birmingham': 11, 'Jacksonville': 16, 'Houston': 8, 'Dallas': 12},
			'Detroit': {'Buffalo': 7, 'Pittsburgh': 6, 'Cincinnati': 4, 'Chicago': 7, 'Duluth': 15},
			'Cincinnati': {'Detroit': 4, 'Pittsburgh': 7, 'Raleigh': 15, 'Knoxville': 6, 'St Louis': 12, 'Chicago': 7},
			'Knoxville': {'Cincinnati': 6, 'Atlanta': 5},
			'Birmingham': {'Atlanta': 3, 'Jacksonville': 9, 'New Orleans': 11, 'Memphis': 6},
			'Atlanta': {'Knoxville': 5, 'Raleigh': 7, 'Savannah': 7, 'Birmingham': 3, 'St Louis': 12},
			'Buffalo': {'New York': 8, 'Pittsburgh': 7, 'Detroit': 7},
			'Pittsburgh': {'Buffalo': 7, 'Washington DC': 6, 'Raleigh': 7, 'Cincinnati': 7, 'Detroit': 6},
			'Boston': {'New York': 3},
			'New York': {'Boston': 3, 'Philadelphia': 0, 'Buffalo': 8},
			'Philadelphia': {'New York': 0, 'Washington DC': 3},
			'Washington DC': {'Philadelphia': 3, 'Norfolk': 5, 'Pittsburgh': 6},
			'Norfolk': {'Raleigh': 3, 'Washington DC': 5},
			'Raleigh': {'Norfolk': 3, 'Savannah': 7, 'Atlanta': 7, 'Cincinnati': 15, 'Pittsburgh': 7},
			'Savannah': {'Raleigh': 7, 'Jacksonville': 0, 'Atlanta': 7},
			'Jacksonville': {'Savannah': 0, 'Tampa': 4, 'New Orleans': 16, 'Birmingham': 9},
			'Tampa': {'Jacksonville': 4, 'Miami': 4},
			'Miami': {'Tampa': 4}
			}

color_map = {
			 'Purple': ['Seattle', 'Portland', 'Boise', 'Billings', 'Cheyenne', 'Denver', 'Omaha'],
			 'Blue': ['San Francisco', 'Los Angeles', 'San Diego', 'Las Vegas', 'Salt Lake City', 'Phoenix', 'Santa Fe'],
			 'Yellow': ['Fargo', 'Duluth', 'Minneapolis', 'Chicago', 'St Louis', 'Cincinnati', 'Knoxville'],
			 'Red': ['Kansas City', 'Oklahoma City', 'Dallas', 'Houston', 'Memphis', 'New Orleans', 'Birmingham'],
			 'Brown': ['Detroit', 'Buffalo', 'Pittsburgh', 'Boston', 'New York', 'Philadelphia', 'Washington DC'],
			 'Green': ['Norfolk', 'Raleigh', 'Savannah', 'Atlanta', 'Jacksonville', 'Tampa', 'Miami']	
			}

power_plants = {
				3: ('oil', 2, 1), 4: ('coal', 2, 1), 5: ('coal/oil', 2, 1), 6: ('garbage', 1, 1), 7: ('oil', 3, 2), 8: ('coal', 3, 2), 
				9: ('oil', 1, 1), 10: ('coal', 2, 2), 11: ('uranium', 1, 2), 12: ('coal/oil', 2, 2), 13: ('wind', 0, 1), 14: ('garbage', 2, 2), 
				15: ('coal', 2, 3), 16: ('oil', 2, 3), 17: ('uranium', 1, 2), 18: ('wind', 0, 2), 19: ('garbage', 2, 3), 20: ('coal', 3, 5), 
				21: ('coal/oil', 2, 4), 22: ('wind', 0, 2), 23: ('uranium', 1, 3), 24: ('garbage', 2, 4), 25: ('coal', 2, 5), 26: ('oil', 2, 5), 
				27: ('wind', 0, 3), 28: ('uranium', 1, 4), 29: ('coal/oil', 1, 4), 30: ('garbage', 3, 6), 31: ('coal', 3, 6), 32: ('oil', 3, 6), 
				33: ('wind', 0, 4), 34: ('uranium', 1, 5), 35: ('oil', 1, 5), 36: ('coal', 3, 7), 37: ('wind', 0, 4), 38: ('garbage', 3, 7), 
				39: ('uranium', 1, 6), 40: ('garbage', 2, 6), 42: ('coal', 2, 6), 44: ('wind', 0, 5), 46: ('coal/oil', 3, 7), 50: ('wind', 0, 6)
				}

resource_map = {
			 'coal': 0,
			 'oil': 0,
			 'garbage': 0,
			 'uranium': 0
			}



def test_nodes():
	for x in city_map:
		for y in city_map[x]:
			assert y in city_map, 'City not found; check spelling %r %r' %x %y.keys()
			assert (city_map[x][y]) == city_map[y][x], 'City is missing bidirectional path %r %r' %x %y[0]
		in_color = False
		for color in color_map:
			assert len(color_map[color]) == 7, 'Cities not zoned into colored regions correctly'
			if x in color_map[color]:
				assert in_color == False, 'Duplicate city %r' %x
				in_color = True
		assert in_color == True, 'City missing %r' %x

def test_plants():
	for x in power_plants:
		assert len(power_plants[x]) == 3, 'Power plant lacking required information: %r' %x[0]
	assert len(power_plants) == 42, 'Power plant missing from list'

def get_cities():
	return city_map
def get_colors():
	return color_map
def get_resources():
	return resource_map
def get_plants():
	return power_plants

#
# Demo functions -- to be deleted from final version
#
def print_cities():
	for x in city_map:
		print(x)
		time.sleep(.1)

def get_city(x):
	if x in city_map:
		print(x, ':')
		for y in city_map[x]:
			print('\tIt costs ', city_map[x][y], ' to connect to ', y)

test_nodes()
test_plants()