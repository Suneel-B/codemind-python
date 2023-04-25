def pair(N,arr):
    evencnt=0
    oddcnt=0
    for i in range(N):
        if(arr[i]%2!=0):
            oddcnt+=1
        else: evencnt+=1
    if oddcnt%2==0 and evencnt%2==0 : return 1
    else : return 0
n = int(input())
li = list(map(int,input().split()))
print(pair(n,li))