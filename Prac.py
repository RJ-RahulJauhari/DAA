def EuclideanGCD(m, n):
    while n != 0:
        r = m % n
        m = n
        n = r
    return m


def ConsecutiveGCD(m, n):
    GCD = None

    if m < n:
        m, n = n, m
    if m % n == 0:
        GCD = n
    else:
        for i in range(m, 1, -1):
            if m % i == 0 and n % i == 0:
                GCD = i
                break
    return GCD


def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


def mergesort(l):
    if len(l) <= 1:
        return l
    mid = int(len(l) / 2)
    left = mergesort(l[:mid])
    right = mergesort(l[mid:])
    return merge(left, right)


def partition(arr, left, right):
    p = arr[right]
    i = left
    j = right - 1

    while i < j:
        while arr[i] < p and i < right:
            i += 1
        while arr[j] > p and j > left:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    if arr[i] > p:
        arr[i], arr[right] = arr[right], arr[i]

    return i


def quicksort(arr, left, right):
    if left < right:
        partition_index = partition(arr, left, right)
        quicksort(arr, left, partition_index - 1)
        quicksort(arr, partition_index + 1, right)
    return arr


def PrimsAlgo():
    INF = 999999999999

    g = [[0, 19, 5, 0, 0],
         [19, 0, 5, 9, 2],
         [5, 5, 0, 1, 6],
         [0, 9, 1, 0, 1],
         [0, 2, 6, 1, 0]]

    # no. of vertices in the graph
    N = 5

    # initializing visited array to 0's to keep track of visited nodes
    visited = [0, 0, 0, 0, 0]

    # initializing edge count to zero
    no_edges = 0

    # starting with the 1st node
    visited[0] = True

    while no_edges < N - 1:

        minimum = INF
        s = 0
        d = 0

        for node in range(N):
            if visited[node]:
                for connect in range(N):
                    if (not visited[connect]) and g[node][connect]:
                        if minimum > g[node][connect]:
                            minimum = g[node][connect]
                            s = node
                            d = connect

        print(s, " connects to ", d, " Weight: ", g[s][d], '\n')
        visited[d] = True
        no_edges += 1


l = [4, 1, 2, 9, 0, 6, 1, 3, 8]
print(mergesort(l))
print(quicksort(l, 0, len(l) - 1))
print(EuclideanGCD(15, 25))
print(ConsecutiveGCD(231, 15))
