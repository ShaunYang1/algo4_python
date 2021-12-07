#!/Users/csc/anaconda3/bin/python
from sortBase import Sort
class SelectSort(Sort):
	
	
	def sort(arr):
		max_length=len(arr)
		for i in range(max_length):
			min=i
			for j in range(i+1,max_length):
				if arr[min]>arr[j]:
					min=j
			
			arr[i],arr[min]=arr[min],arr[i]
		return arr
if __name__=='__main__':
	import sys
	items = []
	for line in sys.stdin:
		items.extend(line.split())
	print('     items: ',items)
	print('sort items: ',SelectSort.sort(items))	 
	assert SelectSort.is_sorted(items)
