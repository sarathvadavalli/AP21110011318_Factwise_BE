# There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.
# In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.
# Your score is the sum of the points of the cards you have taken.
# Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

def score(L, k):
    if(k > len(L)):
        print(sum(L))
    
    i = 0
    j = -1
    s = 0
    while(k > 0):
        if(L[i] > L[j]):
            s += L[i]
            i += 1
        else:
            s += L[j]
            j -= 1
        k -= 1

    return s

L = list(map(int, input().split()))
k = int(input())
res = score(L,k)
print(res)