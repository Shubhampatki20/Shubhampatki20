a=[]
size=int(input("Enter a size on list:"))
for i in range(size):
    b=int(input("Enter a value which needs to be add in LIST:"))
    a.append(b)
print("List is :", a)
sum=0
for i in range(size):
    sum= sum + a[i]
print("Sum of list is :" , sum)