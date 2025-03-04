def findTheWinner(n: int, k: int) -> int:
    arr = []

    for i in range(1, n+1):
        arr.append(i)

    print(arr)

    ind = 0
    count = 1
    while len(arr) > 1:
        if count == k:
            del arr[ind]
            count = 1
        else:
            count += 1
            ind += 1

        if ind >= len(arr):
            ind = 0
    
    return arr[0]


print(findTheWinner(5, 2))