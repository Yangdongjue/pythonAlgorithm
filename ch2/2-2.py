import sys
#sys.stdin=open("input.txt", "rt")

T=int(input())

for i in range(0, T):
    N,s,e,k=map(int, input().split())
    arr = list(map(int,input().split()))
    arr=arr[s-1:e]
    arr.sort()
    print("#{} {}".format(i+1, arr[k-1]))
