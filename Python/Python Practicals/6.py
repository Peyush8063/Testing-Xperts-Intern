while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

#Handling Exception
        
#Grouping Exception
# except (RuntimeError, TypeError, NameError):
#     pass       
        
#Exceptions are handled for printing the error
        
#else is there in try except which gets executed when no error is raised
        
try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    # raise

#try also has finally which will get executed at all cost despite error
    
try:
    raise KeyboardInterrupt
finally:
    print('Goodbye, world!')


#Exception chaining
    
def func():
    raise ConnectionError

try:
    func()
except ConnectionError as exc:
    raise RuntimeError('Failed to open database') from exc

#Predefined cleanup-  like with open in file handling automatically closes file so it is it's predefined clean p action before wrapping up the task
    
try:
    raise TypeError('bad type')
except Exception as e:
    e.add_note('Add some information')
    e.add_note('Add some more information')
    raise
