#Lambda Expression

f= lambda a: a*a 
g=lambda a,b:a+b
print(g(1,2))
print(f(5))


#Filter Map Reduce

nums=[3,6,3,8,4,7,1,0,9]

evenNums= list(filter(lambda a: a%2==0,nums))
evenNums.sort()
print(evenNums)

triples=list(map(lambda a:a*3,evenNums))
print(triples)

from functools import reduce
finalAddition= reduce(lambda a,b:a+b,triples)
print(finalAddition)

from module_Peyush import *

name=str(input("enter your name: "))
intro(name)

import fibo

