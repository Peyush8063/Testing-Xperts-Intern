import fibo

fibo.fibonacci(100)

# we can also import like
# from fibo import fibonacci

# so we could use simply fibonacci(100)

# also there is from module import *
#import all functions except those with underscore

# dir() tells us names which a module defines

print(dir(fibo))
print(dir())
print(dir(__builtins__))