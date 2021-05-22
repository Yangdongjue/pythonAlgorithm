import sys
N= int(input())
M= list(map(int, input().split()))

score=0
scoreSum=0

for i in M:
    if i==1:
        score+=1
        scoreSum+=score
    else : score=0
print(scoreSum)