

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

	return item_selected, 0


def dynamic_programming(capacity, values, weights):
	"""
	Simple dynamic programming algorithm.
	T(n, W) = O(nW), S(n, W) = O(nW); n = number of items, W = knapsack capacity.
	"""
	# Initialization
	n = len(values)
	W = capacity
	weights = [float('-infinity')] + weights	# Make weights zero-indexed
	values = [float('-infinity')] + values		# Make values zero-indexed
	K = [ [0 for _ in xrange(0, W + 1)] for _ in xrange(0, n + 1) ]

	# Fill table for all j, w
	for j in xrange(1, n + 1):
		for w in xrange(1, W + 1):
			if weights[j] > w:
				K[j][w] = K[j - 1][w]
			else:
				K[j][w] = max(K[j - 1][w], K[j - 1][w - weights[j]] + values[j])

	# Trace back in table to determine which items to select
	item_selected = [0 for _ in range(n + 1)]
	w = W
	for j in xrange(n, 0, -1):
		if K[j - 1][w] == K[j][w]:		# Item j was not picked
			item_selected[j] = 0
		else:
			item_selected[j] = 1		# Item j was picked
			w -= weights[j]

	item_selected = item_selected[1:]	# Remove dummy index-zero element
	return item_selected, 1


def memory_efficient_dynamic_programming(capacity, values, weights):
	"""
	A memory-efficient version of the dynamic programming algorithm.
	T(n, W) = O(nW), S(n, W) = O(W); n = number of items, W = knapsack capacity.
	"""
	n = len(values)
	W = capacity
	weights = [float('-infinity')] + weights	# Make weights zero-indexed
	values = [float('-infinity')] + values		# Make values zero-indexed
	
	previous_column = [0 for _ in xrange(0, W + 1)]
	current_column = [0 for _ in xrange(0, W + 1)]
	previous_k = [0 for _ in xrange(0, W + 1)]		# k[w] is the row where the optimal path to
	current_k = [0 for _ in xrange(0, W + 1)]		# column[k] passes through column n/2

	# Find optimal value, column by column.
	for j in xrange(1, n + 1):
		# Advance current column
		previous_column, current_column = current_column, previous_column
		previous_k, current_k = current_k, previous_k

		for w in xrange(1, W + 1):
			if weights[j] > w:
				current_column[w] = previous_column[w]
				current_k[w] = previous_k[w]
			else:
				current_column[w] = max(previous_column[w], previous_column[w - weights[j]] + values[j])
				if previous_column[w] > previous_column[w - weights[j]] + values[j]:
					current_column[w] = previous_column[w]
					current_k[w] = previous_k[w]
				else:
					current_column[w] = previous_column[w - weights[j]] + values[j]
					current_k = previous_k[w - weights[j]]








