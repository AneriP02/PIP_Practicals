#STUDENT ID: 20CE067
#STUDENT NAME: ANERI PANCHAL
#AIM: PRACTICAL-4
#GITHUB LINK: https://github.com/AneriP02/PIP_Practicals.git

n=int(input())
Score=list(map(int,input().split()))
temp=[]
for i in range(n):
    m=max(Score)
    if(Score[i]<m):
        temp.append(Score[i])
    else:
        continue
print(max(temp))


