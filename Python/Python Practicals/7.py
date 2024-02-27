class Student:
    def __init__(self, name, age,rollNo):
        self.name = name
        self.age = age
        self.rollNo=rollNo
    
    def __str__(self):
        return f"{self.name}({self.rollNo})"
    
    def intro(self):
        print("Hello my name is " + self.name + " and my roll no is "+self.rollNo)

s1=Student("Peyush",19,21103092)

print(s1.name,s1.rollNo)
print(s1)
s1.intro()
del s1.age


class StudentCouncilMember(Student):
    def __init__(self, name, age,rollNo, responsibility):
        Student.__init__(self,name,age,rollNo)
        #can also use super()
        self.responsibility=responsibility

    def intro(self):
        print("Hello my name is " + self.name + " and my roll no is "+self.rollNo+ " and I am the "+ self.responsibility)

#iterators
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))