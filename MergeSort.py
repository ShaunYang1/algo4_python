#!/Users/csc/anaconda3/bin/python
from sortBase import Sort
class MergeSort(Sort):
   
    #need to solve left=mid=right case
    def merge(arr,left,right,mid):
        N=right-left
        tmp_list=[0 for i in range(N)]

        ptr_l=left
        ptr_r=mid
        #注意这里两个数组都
        #左闭右开
        for i in range(N):
            if (ptr_l<mid)and(ptr_r<right):
                if arr[ptr_l]<=arr[ptr_r]:
                    tmp_list[i]=arr[ptr_l]
                    ptr_l+=1
                else:
                    tmp_list[i]=arr[ptr_r]
                    ptr_r+=1
            elif (ptr_l==mid) and (ptr_r<right):
                tmp_list[i]=arr[ptr_r]
                ptr_r+=1
            elif (ptr_l<mid) and (ptr_r==right):
                tmp_list[i]=arr[ptr_l]
                ptr_l+=1
            else:
                print('error in merge array')
        
        for i in range(N):
            arr[left+i]=tmp_list[i]


    def mergesort(arr,left,right):
        if(left+1>=right):
            return
        mid = left + (right-left)//2
        MergeSort.mergesort(arr,left,mid)
        MergeSort.mergesort(arr,mid,right)
        MergeSort.merge(arr,left,right,mid)

    
    def sort(arr):
        N = len(arr)
        right = N
        left= 0
        
        MergeSort.mergesort(arr,left,right)
        return arr
        




if __name__=='__main__':
    import sys,random,time
    items = [random.randint(1,100000) for i in range(100000)]
	# for line in sys.stdin:
	# 	items.extend(line.split())
    start=time.time()
    print('     items: ',items)
    print('sort items: ',MergeSort.sort(items))	 
    end=time.time()
    print('performance',end-start,'s')
    assert MergeSort.is_sorted(items)
