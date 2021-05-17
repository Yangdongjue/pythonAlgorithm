import sys
#sys.stdin=open("input.txt", "rt")

N, M = map(int, input().split())
arr=[]
arr2=[]
arrDic={}
for i in range(1,N+1):
    for j in range(1, M+1):
        arr.append(i+j)

arr.sort()
arrSet=list(set(arr))

for i in range(len(arrSet)):
    arrDic[arrSet[i]]=arr.count(arrSet[i])

valueList=list(arrDic.values())
valueList.sort(reverse=True)


for j in arrSet:
    if (arrDic.get(j)==valueList[0]):
        arr2.append(j)


arr2.sort()
for i in arr2:
    print("%d" %(i),end=' ')
