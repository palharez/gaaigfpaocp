def count(arr):
	if not len(arr):
		return 0
	return 1 + count(arr[1:])