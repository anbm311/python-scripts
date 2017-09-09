#this script to find 3 largest numbers

import sys

def printlargest(arr):
    first = -sys.maxsize-1
    second = -sys.maxsize-1
    third = -sys.maxsize-1

    if len(arr) < 3:
        print('enter the valid array len')

    for i in range(len(arr)):
        if arr[i] > first :
            third, second, first = second, first, arr[i]
        elif arr[i] > second :
            third, second = third, arr[i]
        elif arr[i] > third :
            third = arr[i]
    print('first ={0}, second={1}, second={2}'.format(first, second, third))

printlargest([12,13,1,10,34,1])
