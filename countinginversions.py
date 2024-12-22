def mergesort(arr):
    if len(arr) <= 1:
        return arr, []
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    lsort, left_inversions = mergesort(left)
    rsort, right_inversions = mergesort(right)
    
    merged, split_inversions = merge(lsort, rsort)
    
    total_inversions = left_inversions + right_inversions + split_inversions
    
    return merged, total_inversions

def merge(lsort, rsort):
    res = []
    inversions = []
    i = j = 0
    
    while i < len(lsort) and j < len(rsort):
        if lsort[i] > rsort[j]:
            res.append(rsort[j])
            # Record the inversions
            for k in range(i, len(lsort)):
                inversions.append((lsort[k], rsort[j]))
            j += 1
        else:
            res.append(lsort[i])
            i += 1
    
    res.extend(lsort[i:])
    res.extend(rsort[j:])
    
    return res, inversions

# Main code
n = int(input("Enter the number of elements you want to input: "))
arr = []
for i in range(n):
    element = float(input(f"Enter element {i+1}: "))
    arr.append(element)

sorted_array, inversions = mergesort(arr)

print("Sorted array =", sorted_array)
print("Number of inversions =", len(inversions))
print("Inversions:", inversions)
