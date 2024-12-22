def mergesort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]
    lsort=mergesort(left)
    rsort=mergesort(right)
    return merge(lsort,rsort)
def merge(lsort,rsort):
    res=[]
    i=j=0
    while i<len(lsort) and j<len(rsort):
        if lsort[i]>rsort[j]:
            res.append(rsort[j])
            j=j+1
        else:
            res.append(lsort[i])
            i=i+1
    res.extend(lsort[i:])
    res.extend(rsort[j:])
    return res
n=int(input("Enter the number of elements you want to input:"))
arr=[]
for i in range(n):
    element=float(input(f"Enter element {i+1}:"))
    arr.append(element)
sorted_array=mergesort(arr)
print("Sorted array=",sorted_array)