#find a median in given sorted array

def median(arr):
    n=len(arr)
    if n <= 1:
        return None
    elif n % 2 == 1:
        #if len is odd, return middle element as median
        return arr[n//2]
    else:
        #if len is even, return median of two elements
        return (arr[n//2-1]+arr[n//2+1])//2


print(median([15, 20, 45, 80, 90]))
print(median([15, 20, 45, 77, 80, 90]))
