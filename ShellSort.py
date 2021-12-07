#!/Users/csc/anaconda3/bin/python
from sortBase import Sort
class ShellSort(Sort):
	
	def sort(arr):
		N=len(arr)
		h=1 #h有序
		while (h<N/3):
			h=3*h+1
		while (h>=1):
			for i in range(h,N):
				for j in range(i,h-1,-h):
					if arr[j]<arr[j-h]:
						arr[j],arr[j-h]=arr[j-h],arr[j]
					else:
						break
			h=h//3	
		return arr
if __name__=='__main__':
	import sys
	items = []
	for line in sys.stdin:
		items.extend(line.split())
	print('     items: ',items)
	print('sort items: ',ShellSort.sort(items))	 
	assert ShellSort.is_sorted(items)
