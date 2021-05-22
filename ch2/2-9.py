import sys

N= int(input())
K=[]
for i in range(N):
    m=list(map(int, input().split()))
    K.append(m)

J=[]
for i in range(len(K)):
    if K[i][0]==K[i][1]==K[i][2]:
        J.append(10000+K[i][0]*1000)
    elif K[i][0]!=K[i][1] and K[i][0]!=K[i][2] and K[i][1]!=K[i][2]:#모두다를때
        max=K[i][0]
        for i in K[i]: #최대눈 찾기
            if max<i:
                max=i
        J.append(max*100)
    else :
        if K[i][0]==K[i][1]: J.append(1000+K[i][0]*100)
        elif K[i][0]==K[i][2]: J.append(1000+K[i][0]*100)
        else : J.append(1000+100*K[i][1])
output=J[0]
for i in J:
    if output<i:
        output=i
print(output)
