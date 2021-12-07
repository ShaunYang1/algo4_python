#!/Users/csc/anaconda3/bin/python

class Sort:
	def is_sorted(arr):
		for i in range(1,len(arr)):
			if arr[i]<arr[i-1]:
				return False
		return True
