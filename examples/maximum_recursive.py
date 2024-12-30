def maximum(arr):
	if not arr:
		return 0
	
	maxi = maximum(arr[1:])
	
	return arr[0] if arr[0] > maxi else maxi