def sort_dictionary(dct):
	sorted_items = sorted(dct.items(), key=lambda x: x[1][1])
	result = [(k, v[0]) for k, v in sorted_items]
	return result
