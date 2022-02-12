#STUDENT ID: 20CE067
#STUDENT NAME: ANERI PANCHAL
#AIM: PRACTICAL-7
#GITHUB LINK: https://github.com/AneriP02/PIP_Practicals.git

def Lapindrome(str):
    strlen = len(str)
    if(strlen%2==0):
        a = str[:(strlen//2)]
        b = str[(strlen//2):]
    else: 
        a = str[:(strlen//2)]
        b = str[(strlen//2)+1:]
    la = list(a)
    la.sort()
    lb = list(b)
    lb.sort()
    if (la==lb):
        print("YES")
    else:
        print("NO")

t = int(input())

for i in range(t):
    text =  input()
    Lapindrome(text)