n=int(input("Enter a number:"))
fact=1
if(n<0):
    print("No factorial for -Ve num")
elif(n==0):
   print("factorial of 0 is 1")
else:
     for i in range(1,n+1):
         fact=fact*i
     print("factorial of", n,"is",fact)

