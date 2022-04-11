a = int(input("enter number :"))

for i in range(2,a):
    if(a%i)==0:
        print("not a prime")
        break
    else:
        print(" prime")
        break