class Insertsort:
    @classmethod
    def sort(cls,arr):
        maxlen=len(arr)
        for i in range(1,maxlen):
            for j in range(i,0,-1):
                if (arr[j-1]>arr[j]):
                    arr[j],arr[j-1]=arr[j-1],arr[j]
                else:
                    break
        return arr
    @classmethod
    def is_sorted(cls,arr):
        for i in range(1,len(arr)):
            if arr[i-1]>arr[i]:
                return False
        return True

if __name__=='__main__':
    import sys

    items=[]
    for line in sys.stdin:
        items.extend(line.split())
    print('     items',items)
    print('sort items',Insertsort.sort(items))
    assert Insertsort.is_sorted(items)