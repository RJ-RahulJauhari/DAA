def SubsetSum(set, n, sum):
    if sum == 0:
        return True
    if n == 0 and sum != 0:
        return False
    if set[n - 1] > sum:
        return SubsetSum(set, n - 1, sum)
    return SubsetSum(set, n - 1, sum) or SubsetSum(set, n - 1, sum - set[n - 1])


set = [2, 1, 4, 9, 3, 0, 5, 6]
sum = 11

if SubsetSum(set, len(set), sum):
    print("Found")
else:
    print("Not Found")
