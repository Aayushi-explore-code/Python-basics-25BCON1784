a=0
b=1
next
for i in range(10):
    print(a, end=" ")
    next=a+b
    a=b
    b=next
