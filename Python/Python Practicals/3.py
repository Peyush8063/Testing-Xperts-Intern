#list functions

punjabCities=['mansa','bathinda','moga','barnala','fazilka']
print(punjabCities)
punjabCities.append('amritsar')
print(punjabCities)
cities=['pathankot','ludhiana','patiala']
punjabCities.extend(cities)
print(punjabCities)
punjabCities.insert(2,'jalandhar')
print(punjabCities)
punjabCities.remove('fazilka')
print(punjabCities)
punjabCities.pop()
print(punjabCities)
punjabCities.sort()
print(punjabCities)
punjabCities.reverse()
print(punjabCities)
l=punjabCities.copy()
l.clear()
print(l)
punjabCities.append('mansa')
print(punjabCities.count('mansa'))

# to use queue import deque from collections
from collections import deque
queue = deque(["Eric", "John", "Michael"])
print(queue.popleft()) 


#list comprehension

cubes=[x**3 for x in range(10)]
a=[(x, y) for x in [1,2,3] for y in [3,2,1] if x != y]
print(a)
b=[[1,2,3], [4,5,6], [7,8,9]]
print([num for elem in b for num in elem])
print([[row[i] for row in b] for i in range(3)])

del cubes

t="Peyush",3092,8063,8.43
# tuples are immutable 
print(t)

x=set('Peyush')
y=set('anish')

print(x)
print(x-y,x|y,x^y,x&y)

# in and not in used to tell whether thing is in other specified thing or not

# dict() constructor

# key and value can be together retrieved in looping via dict.items()
# .enumerate() for accessing index as well as value together
# .zip() for looping 2 or more sequence at same time