def sum2(arr):
	out = 0
	if len(arr)==1:
		return arr[0]
	l = len(arr)//2
	out += sum2(arr[0:l])
	out += sum2(arr[l:])
	return out

print(sum2([1,2,4,8,16,32,64,128]))