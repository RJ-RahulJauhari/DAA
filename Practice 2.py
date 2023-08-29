def SubsetSum(set,sum,n):
    if sum == 0:
        return True
    if n == 0 and sum != 0:
        return False
    if set[n-1] > sum:
        return SubsetSum(set,sum,n-1)
    return SubsetSum(set,sum,n-1) or SubsetSum(set,sum - set[n-1],n-1)

a = [1,9,0,2,4,7,3]
sum = 100

if SubsetSum(a,sum,len(a)):
    print("Found")
else:
    print("Rejected")