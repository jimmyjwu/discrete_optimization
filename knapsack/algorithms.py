def fill_in_order(capacity, values, weights):
	"""
	Trivial greedy algorithm (included with problem folder).
	Takes items in order until the knapsack is full.
	"""
	number_of_items = len(values)
	total_value = 0
	total_weight = 0
	item_selected = []

	for i in range(number_of_items):
		if total_weight + weights[i] <= capacity:
			item_selected.append(1)
			total_value += values[i]
			total_weight += weights[i]
		else:
			item_selected.append(0)

	return item_selected