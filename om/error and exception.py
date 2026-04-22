try:
    x=int("abc")
except  ValueError:
    print("invalid number entered")

try:
    a=10/0
except ZeroDivisionError:
    print("you cannot divide by zero")

try:
    a=[1,2,3,4,5]
    print(a[7])
except IndexError:
    print("invalid index provided")

try:
    a=25/0
    print(a)
except ZeroDivisionError:
    print("you cannot divide by zero")
