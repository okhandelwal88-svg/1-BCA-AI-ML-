
try:
 list=[]
 for i in range(1,3):
    user=int(input("enter your number"))
    list.append(user)
    print(list)
except ValueError:
    print("not an integer value")


