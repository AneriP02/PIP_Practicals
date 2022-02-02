#STUDENT ID: 20CE067
#STUDENT NAME: ANERI PANCHAL
#AIM: PRACTICAL-5 _ SWAP CASE
#GITHUB LINK: https://github.com/AneriP02/PIP_Practicals.git

K = input()
new_K=""
for i in range (len(K)):
    if K[i].isupper():
        new_K+=K[i].lower()
    else:
        new_K+=K[i].upper()
print(new_K)