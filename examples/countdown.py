def countdown(i):
	print(i)
	if i <= 0: # Base case
		return
	else:
		return countdown(i-1)


if __name__ == '__main__':
    countdown(5)