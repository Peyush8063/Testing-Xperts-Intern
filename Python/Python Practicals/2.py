n=int(input("Enter a number:"))

def check(num):
    if num>=50:
        return("Pass")
    elif num>33:
        return("Re-appear")
    else:
        return("Fail")

print(check(n))

result=["pass","fail","re-appear"]
for r in result:
    print(r,len(r))

markList={"A":51,"B":40,"C":30}

faiureList=[]
for person,marks in markList.items():
    if check(marks)=="Fail":
        faiureList.append(person)

print(list(range(5,9)))

print(list(range(5,9,2)))

a=['Peyush','PJ','abc','def']

for i in range(len(a)):
    print(i,a[i])

# else in for loops 
    
    for n in range(2, 10):
        for x in range(2, n):
            if n % x == 0:
                print(n, 'equals', x, '*', n//x)
                break
    else:
        # here this else if for loop . it executes when no break occurs
        print(n, 'is a prime number')

#pass statement do nothing . used when program do no action
        
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
        

# default argument value
def promote(name,result="pass"):
    if result=="pass":
        print(f"{name} is promoted!")
    else:
        print(f"{name} is not Promoted!")

promote("Peyush")
promote("abc","Fail")

# keyword argument is of form kwarg=value
# eg- def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):

# positional where arguments are assigned acc to position vs eyword where keyword is mentioned along with the argument

# def cheeseshop(kind, *arguments, **keywords):
# here *argumets means it can take any no of args and **keywords mean it can take keyword args as a dict

# def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
#       -----------    ----------     ----------
#         |             |                  |
#         |        Positional or keyword   |
#         |                                - Keyword only
#          -- Positional only

#unpacking

# args = [3, 6]
# list(range(*args))

# def parrot(voltage, state='a stiff', action='voom'):
#     print("-- This parrot wouldn't", action, end=' ')
#     print("if you put", voltage, "volts through it.", end=' ')
#     print("E's", state, "!")

# d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
# parrot(**d)
