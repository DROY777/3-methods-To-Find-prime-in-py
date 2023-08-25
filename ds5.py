# prime in range
'''n=int(input("Enter Start"))
g=int(input("Enter End"))

for num in range(n,g+1):
     if num>1:
        for i in range(2,num):
          if (num%i==0):
            break
          else: 
             print(num) '''

# prime m1
'''n=int(input("Enter no:"))
f=False
if n<1:
   print(n,"is not prime")
elif n>1: 
  for i in  range(2,n):
     if(n%i==0):      
         f=True
         break
if f:
 print(n,"is not prime")
else:
 print(n,"is prime")'''     

# prime m2
n=int(input("Enter no:"))
if n<=1:
    print(n,"is not a Prime")
elif n>1:
     for i in range(2,n):
        if(n%i==0):
          print(n,"is not a prime")
          break
     else:
         print(n,"is a prime no")         
             
         