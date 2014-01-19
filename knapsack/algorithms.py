

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


def calculate_optimal_midpoint(capacity, values, weights):
	"""
	A memory-efficient version of the dynamic programming algorithm that returns
	the value k such that (k, n/2) is in the optimal path through the DP table.
	T(n, W) = O(nW), S(n, W) = O(W); n = number of items, W = knapsack capacity.
	"""
	n = len(values)
	W = capacity
	weights = [float('-infinity')] + weights	# Make weights zero-indexed
	values = [float('-infinity')] + values		# Make values zero-indexed
	
	previous_column = [0 for _ in xrange(0, W + 1)]
	current_column = [0 for _ in xrange(0, W + 1)]
	previous_k = [k for k in xrange(0, W + 1)]		# k[w] is the row where the optimal path to
	current_k = [k for k in xrange(0, W + 1)]		# column[k] passes through column n/2

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
				if previous_column[w] > previous_column[w - weights[j]] + values[j]:
					current_column[w] = previous_column[w]
					if j > n / 2:
						current_k[w] = previous_k[w]
				else:
					current_column[w] = previous_column[w - weights[j]] + values[j]
					if j > n / 2:
						current_k[w] = previous_k[w - weights[j]]

	return current_k[W]

def find_optimal_path(capacity, values, weights):
	n = len(values)
	W = capacity

	if n == 2:
		if W - weights[0] > 0:
			return [W - weights[0], W]
		else:
			return [W, W]
	else:
		k = calculate_optimal_midpoint(capacity, values, weights)

		left_path = find_optimal_path(k, values[:n/2 + 1], weights[:n/2 + 1])
		right_path = find_optimal_path(W - k, values[n/2:], weights[n/2:])
		for i in xrange(len(right_path)):
			right_path[i] += k

		return left_path + right_path[1:]


def evaluate_decision_variables(optimal_weights, capacity, weights):
	previous_total_weight = optimal_weights[0]
	for i in xrange(len(optimal_weights)):
		optimal_weights[i] -= previous_total_weight
	optimal_weights = optimal_weights[1:] + [capacity if previous_total_weight >= weights[-1] else optimal_weights[-1]]
	decision_variables = []

	for current_total_weight in optimal_weights:
		if current_total_weight > previous_total_weight:
			decision_variables += [1]
			previous_total_weight = current_total_weight
		else:
			decision_variables += [0]

	return decision_variables

def memory_efficient_dynamic_programming(capacity, values, weights):
	optimal_path = find_optimal_path(capacity, values, weights)
	print(optimal_path)
	decision_variables = evaluate_decision_variables(optimal_path, capacity, weights)
	return decision_variables, 1

