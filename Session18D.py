# Knapsack
# >> Bit Pattern
"""
def ks(n,C):
    #if arr[n][C]!=undefined:
        #return arr[n][C]
    if n==0 or C ==0:
        result = 0
    elif w[n]>c:
        result = ks(n-1,C)
    else:
        tmp1 = ks(n-1,C)
        tmp2 = v[n] + ks(n-1, C-w[n])
        result = max(tmp1, tmp2)
    #arr[n][C]= result
    return result
v = [5, 3, 5, 3, 2]
w = [1, 2, 4, 2, 5]
C = 10
n = len(v)
print(ks(n,C))
"""


# A Dynamic Programming based Python Program for 0-1 Knapsack problem
# Returns the maximum value that can be put in a knapsack of capacity W
def knapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]

    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    return K[n][W]

# Driver program to test above function
val = [4000, 3500, 1800, 400, 1000, 200]
wt = [20, 20, 9, 4, 2, 1]
W = 20
n = len(val)
print(knapSack(W, wt, val, n))