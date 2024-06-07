# Program to print positive numbers 
l1= list(map(int,input ("enter the list").split())) #takes list input 
l2=[]
print(l1)
for i in l1:
    if i>0:   #checks whether the number is positive 
        l2.append(i)
print(l2)