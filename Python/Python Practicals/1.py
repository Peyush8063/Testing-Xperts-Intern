# we can use \ to escape and to quote a quote

str='didn\'t'
print(str)


# \n for new line \t for tab

# strings can be concatenated
# 0 based indexing and negative indexing is there in str

print(str[2:])

# strings are immutable

print(len(str))

l=[1,2,3,4]

print(l[2:])
# lists can be concatenated
# lists are immutable

l.append(5)
l[1:3]=[]
print(l)
l[:]=[] # clearing the list
print(l,len(l))

#nested lists 
p=[l,1,2]
print(p)
l.append(1)
print(p[0][0])
