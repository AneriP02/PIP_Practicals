print("-----------------**--DICTIONARY--**---------------")
print("-->Task (a): ")
#To check whether the given key already exists in a Dictionary:
D1={1:"Aneri",2:"Panchal",3:"CE",4:"CSPIT",4:"Jamnagar"}
def key_in(n):
    if n in D1:
        print(n," is present in the given dictionary.")
    else:
        print(n," is not present in the given dictionary.")
key_in(2)
key_in(5)

#-------------------------------------------------
print("\n\n-->Task (b): ")
#To merge two python dictionaries
D2={'a':"Hello",'b':"Python",'c':"Charusat"}
def Merge_D(dict1,dict2):
    return(dict1.update(dict2))
print("Dictionary1: ",D1)
print("Dictionary2: ",D2)
Merge_D(D1,D2)
print("After merging Dictionary 1 and Dictionary 2: ",D1)

#----------------------------------------------
print("\n\n-->Task (c): ")
#To sum all the items in the dictionary
def Sum(Dictionary):
    l=[]
    for i in Dictionary:
        l.append(Dictionary[i])
    Final_sum=sum(l)
    return Final_sum
D3={'a':101,'b':102,'c':103}
print("Dictionary: ",D3)
print("Sum of all the items in the dictionary: ", Sum(D3))

#------------------------------------------------
print("\n\n-->Task (d):")
#To add a new key to the dictionary
Sample_D={0:10,1:20}
print("Dictionary before update: ",Sample_D)
Sample_D[2]=30
print("Dictionary after adding new key: ",Sample_D)

#-----------------------------------------------
print("\n\n-->Task (e):")
#To concatenate following dictionaries to create a new one.
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50, 6:60}
dict4={}
print("Dictionary 1: ",dic1)
print("Dictionary 2: ",dic2)
print("Dictionary 3: ",dic3)
for i in [dic1,dic2,dic3]:
    dict4.update(i)
print("New dictionary after concatenation: ",dict4)

#-------------------*******************-----------------------------
print("\n\n------------------------**--TUPLES--**---------------------")
print("-->Task (a):")
#To create a tuple with different data types.
T1=("Aneri",1 ,2.5 ,True) #diff datatypes 
print("Tuple with different data types: ",T1)

#--------------------------------------------------------
print("\n\n-->Task (b):")
#To create a tuple with numbers and print one item.
T2=(1,2,3,4,5)
item=T2[3]
print("Tuple: ",T2)
print("One item of the tuple: ",item)

#-------------------------------------------------------
print("\n\n-->Task (c):")
#To add an item in a tuple.
print("Tuple: ",T2)#before adding element.
l1=list(T2)
l1.append(6)
T3=tuple(l1)
print("Tuple after adding an element: ",T3)

#-------------------------------------------------------
print("\n\n-->Task (d):")
#To convert a tuple to a string.
T4=('a','n','e','r','i')
Str=''
for i in T4:
    Str=Str+i
print("After conversion of tuple to string: ",Str)

#-------------------------------------------------------
print("\n\n-->Task (e):")
#To find the length of a tuple.
T5=('a','b','c','d','e','f')
print("Tuple: ",T5)
length=len(T5) #using len() function
print("The length of the Tuple is: ",length)

#-------------------*******************-----------------------------
print("\n\n--------------------**--SETS--**---------------------")
print("-->Task (a):")
#To add member(s) in a set and clear a set
Set=set()#empty set
Set.add("abc")#add single element
Set.update(["xyz","pqr"])#add multiple elements
print("The set: ",Set)
Set.clear() #clear a set
print("Set after clear() function: ",Set)

#-------------------------------------------------
print("\n\n-->Task (b):")
#To remove an item from a set if it is present in the set.
S1={1,2,'abc','aneri','charusat'}
print("The set: ",S1)
S1.discard(2)
print("Set after removing an item 2 is : ",S1)
S1.discard(4) #when use discard(), it will not give any error if an element is not present
print("Set after removing an item 4 is: ",S1)
#S1.remove(3) #when use remove() , it will give error if an element is not present 

#------------------------------------------------------
print("\n\n-->Task (c):")
#To create an intersection, Union, difference of sets.
A={0,1,2,4,5,8}
B={2,3,4,6,9,0}
print("Set1: ",A)
print("Set2: ",B)
print("Intersection of Set1 and Set2: ",A.intersection(B)) # AandB
print("Union of Set1 and Set2: ",A.union(B)) # AorB
print("Difference of Set1 and Set2: ",A.difference(B)) #A-B

#------------------------------------------------------
print("\n\n-->Task (d):")
#To find maximum and the minimum value in a set.
S2={1,3,5,9,10,20,30}
print("Set: ",S2)
print("Maximum value from set: ",max(S2))
print("Minimum value from set: ",min(S2))

#-----------------------------------------------------
print("\n\n-->Task (e):")
#To find the most common elements and their counts from list, tuple, dictionary.
from collections import Counter
List=["pink","blue","orange","blue","red","blue"]
count_list=Counter(List)
count_list.most_common(1)
print("The list is: ",List)
print("The most common elememt and its count: ",count_list.most_common(1))

Tuple=('Apple','Orange','Apple','Banana','Grapes')
count_tuple=Counter(Tuple)
print("\nThe Tuple: ",Tuple)
print("The most common elememt and its count: ",count_tuple.most_common(1))

Dictionary={1:2,2:4,3:1,4:4,5:6}
D_List=list(Dictionary.values())
count_dict=Counter(D_List)
print("The Dictionary: ",Dictionary)
print("The most common elememt and its count: ",count_dict.most_common(1))