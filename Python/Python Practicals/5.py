name="Peyush"
year=2004
print(f"My name is {name} and I was born in year {year}")

# .format() is also a way for formatting

print("My name is {} and I was born in year {}".format(name,year))

#str() vs repr()
# The str() function is meant to return representations of values which are fairly human-readable, while repr() is meant to generate representations which can be read by the interpreter


import math
print(f'The value of pi is approximately {math.pi:.3f}.')
#here .3 specify till 3 decimal points

animals = 'eels'
print(f'My hovercraft is full of {animals}.')
print(f'My hovercraft is full of {animals!r}.')

# '!a' applies ascii(), '!s' applies str(), and '!r' applies repr()

bugs = 'roaches'
count = 13
area = 'living room'
print(f'Debugging {bugs=} {count=} {area=}')

print('This {food} is {adjective}.'.format(
      food='spam', adjective='absolutely horrible'))


# h = open('f', 'w', encoding="utf-8")
#Use with as with automatically closes the file

with open('f.txt','r+' ,encoding="utf-8") as g:
    print(g.read())
    g.seek(0,1)
    g.write("Bye")

# another method is .readline(), .close()
    

import json
x = [1, 'simple', 'list']
print(json.dumps(x))
