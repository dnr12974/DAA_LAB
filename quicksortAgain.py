def partition(array,low,high):
    pivot=array[low]
    i=low+1
    for j in range(low+1,high+1):
        if array[j]<=pivot:
            array[i],array[j]=array[j],array[i]
            i=i+1
    array[low],array[i-1]=array[i-1],array[low]
    return i-1
def quicksort(array,low,high):
    if low<high:
        pi=partition(array,low,high)
        quicksort(array,low,pi-1)
        quicksort(array,pi+1,high)
n=int(input("Enter the number of elements you want to input:"))
array=[]
for i in range(n):
    element=float(input(f"Enter the element {i+1}:"))
    array.append(element)
quicksort(array,0,len(array)-1)
print("Sorted array=",array)