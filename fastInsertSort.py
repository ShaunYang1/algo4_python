#!/Users/csc/anaconda3/bin/python

from sortBase import Sort
class fastInsertSort(Sort):
        def sort(arr):
                max_length=len(arr)
                for i in range(1,max_length):
                        item=arr[i]
                        target=i
                        for j in range(i,0,-1):
                                if(arr[j-1]>item):
                                        arr[j]=arr[j-1]
                                        target=j-1
                                else:
                                        break
                        arr[target]=item                        	
                return arr
if __name__=='__main__':
        import sys
        items = []
        for line in sys.stdin:
                items.extend(line.split())
        print('     items: ',items)
        print('sort items: ',fastInsertSort.sort(items))
        assert fastInsertSort.is_sorted(items)
