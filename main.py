import random
def hanoi(ndisks, startPeg, endPeg, usePeg):
 if ndisks > 0:
  hanoi(ndisks-1, startPeg, usePeg, endPeg)
  print ("Move disk", ndisks, "from peg", startPeg,"to peg", endPeg)
  hanoi(ndisks-1, usePeg, endPeg, startPeg)


def fastpower(a,n):
 res=1
 while (n>0):
   if (n%2==1):
     res=res*a
   #print (n, a, res)
   n=n//2
   a=a*a
 return res


def fastmodpower(a,n,p):
 res=1
 while (n>0):
  if (n%2==1):
   res=res*a % p
  #print (n, a, res)
  n=n//2
  a=a*a % p
 return res



def fermat_test(b,c=None,d=None):
  if((c is not None) and (d is not None)):
   num = fastpower(b,c) + d
   for x in range(1,30):
    a = random.randint(1,num-1)
    if(fastmodpower(a,num-1, num) != 1):
     return 'not prime'
   
   return 'prime'
  else:
   num = b
   for x in range(1,30):
     a = random.randint(1,num-1)
     print(a)
     if(fastmodpower(a,num-1, num) != 1):
       print(fastmodpower(a,num-1, num))
       print(a)  
       return 'not prime'
     
   return 'prime'
    


