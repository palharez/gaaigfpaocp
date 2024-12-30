def sum(arr):
	if not len(arr):
		return 0
	return arr[0] + sum(arr[1:])