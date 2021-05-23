import sys
N= int(input())
M=list()
for i in range(N):
    O=input().upper()
    M.append(O)
P=0
for i in M:
   P+=1 
   for j in range(len(i)):
        if i[j]!=i[len(i)-1-j]:
            print("#{} NO".format(P))
            break
        elif j==len(i)-1:
            print("#{} YES".format(P))
