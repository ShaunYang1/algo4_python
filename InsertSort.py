#!/Users/csc/anaconda3/bin/python

from sortBase import Sort
class InsertSort(Sort):
        def sort(arr):
                max_length=len(arr)
                for i in range(1,max_length):
                        for j in range(i,0,-1):
                                if(arr[j-1]>arr[j]):
                                        arr[j],arr[j-1]=arr[j-1],arr[j]
                                else:
                                        break	
                return arr
if __name__=='__main__':
        import sys
        items = []
        for line in sys.stdin:
                items.extend(line.split())
        print('     items: ',items)
        print('sort items: ',InsertSort.sort(items))
        assert InsertSort.is_sorted(items)
