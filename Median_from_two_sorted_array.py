def getMedian(arr1, arr2, n):
    i, j = 0, 0
    m1, m2 = -1, -1
    for count in range(0, n+1):
        if i == n:
            m1 = m2
            m2 = arr2[0]
            break
        elif j == n:
            m1 = m2
            m2 = arr1[0]
            break
        if arr1[i] < arr2[j]:
            m1 = m2
            m2 = arr1[i]
            i=i+1
        else:
            m1 = m2
            m2 = arr2[j]
            j=j+1
    return (m1+m2)//2
            


if __name__ == '__main__':
    arr1 = [1, 12, 15, 27, 30, 57]
    arr2 = [2, 13, 17, 38, 45, 64]
    #arr1 = [1]
    #arr2 = [2]
    if len(arr1) == len(arr2):
        n = len(arr1)
    print(getMedian(arr1, arr2, n))
