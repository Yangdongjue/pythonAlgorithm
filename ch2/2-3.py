import sys
#sys.stdin=open("input.txt", "rt")

N, K = map(int, input().split())
arr=list(map(int,input().split()))
arr2=[]; #res=set()로 집합선언가능
for i in range(0,len(arr)-2):
    for p in range(i+1, len(arr)-1):
        for q in range(p+1, len(arr)):
           arr2.append(arr[i]+arr[p]+arr[q])

arr2=set(arr2)
arr2=list(arr2)

arr2.sort() #res.sort(reverse=True)로 하면 내림차순 가능
arr2.reverse()

print(arr2[K-1])