def count(arr):
	counter = 0
	if len(arr)==1:
		return 1
	l = len(arr)//2
	counter+=count(arr[:l])
	counter+=count(arr[l:])
	return counter

print(count([1,2,4,8,16,32,64,128]))