def binary_search(arr,k):

	if len(arr)==1:
		if arr[0] == k:
			return True
		else:
			return False
	l = len(arr)//2
	if binary_search(arr[:l],k):
		return True
	if binary_search(arr[l:],k):
		return True
	return False
print(binary_search([1,2,4,8,16,32,64,128],128))