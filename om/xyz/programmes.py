def numbers(n):
    n=int(input("enter your number"))
    b=[]
    c=[]
    for i in range(1,n+1):
        if i%2==0:
            b.append(i)
        else :
            c.append(i)
    print(b,c)

def div(a,b):
    if a>b:
        print("yes")
    else:
        print("no")
        