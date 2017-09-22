# roate the array left and right

from collections import deque

def leftrotate(leftarr, n):
    d = deque(leftarr)
    d.rotate(-2)
    print(list(d))
    
def rightrotate(rightarr, n):
    d = deque(rightarr)
    d.rotate(2)
    print(list(d))

def method2(arr, n):
    if len(arr) == 0:
        return arr
    y =n % len(arr)
    return arr[y:] + arr[:y]
  
if __name__ == "__main__":
    arr1=[1, 2, 3, 4, 5, 6, 7]
    arr2=[1, 2, 3, 4, 5, 6, 7]
    leftrotate(arr1, 2)
    rightrotate(arr2, 2)
    print(method2(arr1, 2))
    print(method2(arr1, -2))
    
