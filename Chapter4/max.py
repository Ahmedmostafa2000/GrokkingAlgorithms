def max2(arr):
	out = 0
	if len(arr)==1:
		return arr[0]
	l = len(arr)//2
	first = max2(arr[:l])
	out = [first,out][out>first]
	second = max2(arr[l:])
	out = [second,out][out>second]
	return out
	
print(max2([1,128,2,4,8,16,32,64]))