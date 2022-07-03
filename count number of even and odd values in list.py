a=[]
size=int(input("Enter the size of LIST : "))
for i in range(size):
    b=int(input("Enter the element of array : "))
    a.append(b)
print("LIST is : ",a)
even=0
odd=0
for i in range(size):
    if(a[i]%2==0):
        even=even+1
    else:
        odd=odd+1
print("Numer of even is : ",even,"number of odd is : ",odd)