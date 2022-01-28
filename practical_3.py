#STUDENT ID: 20CE067
#STUDENT NAME: ANERI PANCHAL
#AIM: PRACTICAL-3
#GITHUB LINK: https://github.com/AneriP02/PIP_Practicals.git

K=int(input())
Room_list=list(map(int,input().split()))
n=len(Room_list)
temp_l=[]
Room_list.sort()
count=0
print(Room_list)
i=0
while(i<n):
    count=Room_list.count(Room_list[i])
    if(count==K):
        i=i+K
    else:
        print(Room_list[i])
        break
