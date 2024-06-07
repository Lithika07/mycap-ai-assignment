# A program to illustrate different set operations
s1 = set(map(int, input("enter set 1 elements: ").split()))
s2= set(map(int,input("enter set 2 elements: ").split()))
print('Union',s1.union(s2))
print('Intersection',s1.intersection(s2))
print('Difference',s1.difference(s2))
print('Symmetric difference',s1.symmetric_difference(s2))