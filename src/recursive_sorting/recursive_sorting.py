# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    a = 0
    b = 0

    for k in range(elements):
        if a >= len(arrA):
            merged_arr[k] = arrB[b]
            b += 1
        elif b >= len(arrB):
            merged_arr[k] = arrA[a]
            a += 1
        elif arrA[a] < arrB[b]:
            merged_arr[k] = arrA[a]
            a += 1
        else:
            merged_arr[k] = arrB[b]
            b += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    if len( arr ) > 1:
        mid = len(arr) // 2
        # recursively call merge_sort() on LHS
        # recursively call merge_sort() on RHS
        # left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        # merge sorted pieces
        arr = merge(left, right)
    return arr

# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    left = arr[start:mid+1] # +1 includes the right index
    right = arr[mid+1: end+1] # +1 includes the right index
    i = 0
    j = 0
    k = start
    for l in range(k,end+1):
        if j >= len(right) or (i < len(left) and left[i] < right[j]):
            arr[l] = left[i]
            i = i + 1
        else:
            arr[l] = right[j]
            j = j + 1  
    return arr


def merge_sort_in_place(arr, l, r):
    if r - l > 0:
        mid = int((l+r)//2)
        merge_sort_in_place(arr,l,mid)
        merge_sort_in_place(arr,mid+1,r)
        merge_in_place(arr,l,mid,r)
    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
