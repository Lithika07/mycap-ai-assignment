# program to generate fibonacci series 
a=0
b=1
n=int(input("enter the no. of terms you want in fibonacci series: "))
if n==1:
    print(a)
elif n==2:
    print(b)
elif n>2:
    print(a)
    print(b)
    for i in range(3,n+1):
        c=a+b
        print(c)
        a=b
        b=c
        
