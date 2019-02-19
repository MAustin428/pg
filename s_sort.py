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


print(order_plants([1,2,3]))

