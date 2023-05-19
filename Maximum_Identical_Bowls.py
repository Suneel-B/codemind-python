def maxi(N,arr):
    s=0
    for i in arr:
        s+=i
    for i in range(N,-1,-1):
        if s%i==0:
            return i
    return 1
n = int(input())
li = list(map(int,input().split()))
print(maxi(n,li))