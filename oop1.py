'''class  person:        #1st example of oops..
    def __init__(self,name,age):
        self.name=name
        self.age=age
person1=person("Atul",19)
person2=person("Jarvis",31)
print(person1.name,person1.age)   
print(person2.name,person2.age)'''

'''class person:
    pass
person1=person()
print(person1) #2nd example of oops'''

'''#3rd example of oops
class person:
    def display(self):
        print("Hello")
person1=person()
person1.display()'''

'''#4th example of error showing
# TypeError: display() takes 0 positional arguments but
# 1 was given:
class person:
    def display():
        print("Hello")
#main
p=person()
p.display()'''

'''#5th example for init:
class person:
    def __init__(self,name):
        self.name=name   #for initialing the object we here used init method
    def display(self):   #Here and anywhere the self is due to diffrentiate between instence variable and local variable
        print("Hello",self.name)
        #Here the self.name is intance variable of object person1 and name is local variable to class.
person1=person("Atul")
person1.display()'''

'''#6th example 
 
class person:
    def __init__(self,name):
        self.name=name 
        name="John"#local variable to class
        print(name)   #for initialing the object we here used init method
    def display(self):   #Here and anywhere the self is due to diffrentiate between instence variable and local variable
        print("Hello",self.name)
        #Here the self.name is intance variable of object person1 and name is local variable to class.
person1=person("Atul")
person1.display()'''

'''
#7th example:

class person:
    def __init__(self,name):
        self.name=name 
    def display(self):  
        print("Hello",self.name)

person("amul").display()
person("Jenny").display()# This is a way of writig 
#without makin objectof diffrent name in example #6 person1 like okey
'''
#Till here amulys program of oops is lecture 2.. okey

'''#example 8 of class variable example::::------okey

#lect3:
class student:
    clg='xyz'  #class variable
    def __init__(self,rollno,name):
        self.rollno=rollno
        self.name=name
        
    def display(self):
        print("Student Name",self.name)
        print("Student roll number",self.rollno)
        print("college:",student.clg)

student1=student("xyz001","ATul")
student2=student("xyz002","john")

student1.display()
student2.display()   '''

#example 9: for avoiding to pass the self argument 
# we can use @staticmethod than we need not write self..

'''
class person:
    @staticmethod
    def display():    #here in ( ) wenot write self because we write @staticmethod before..
        print("Hello")
p=person()
p.display()
       '''
#lecture 4:

#Inheriten
#Encapsulation
#polymorphism 

'''basic Syntax
For Inheritance:

class baseclass:
    base_class_body

class deiveclass(baseclass):
    derived_class_body
'''

#now A code of that can be converted into inheritance:
#example 10:
'''
class animal:
    def eating(self):
        print("Eating")
class dog:
    def eating(self):
        print("Eating")  #in this code we write the eating unnessarly we can derived its character fron animal class..
    def bark(self):
        print("Bark")
d=dog()
d.eating()
d.bark()
'''
#now the good programm by using inheritance of example 10:
'''
class animal:
    def eating(self):
        print("Eating")
class dog(animal):
    def bark(self):
        print("Bark")
d=dog()
d.eating()
d.bark()
'''

#Example 11

#Anyother example of inheritance by using init method:

'''
class animal:
    def __init__(self,name):
        self.name=name
class dog(animal):
    def display(self):
        print(self.name)
        
d=dog("babyDog")
d.display()

'''
#lecture 5:
#Multilaevel inheritance:
#IN this example P1 have all the charater of class person and employee and the character is display and printing respectively..
#so when we used p1.display and p1.printing it takes the characters from their parent class or base class..

#Example 12  code:
'''
#base class
class person:
    def display(self):
        print("Hello,this is class person")

#derived class 1

class employee(person):
    def printing(self):
        print("hello,this is derived class employee")

#derived class 2

class programmer(employee):
    def show(self):
        print("Hello,this is another derived class programmer")

p1=programmer()
p1.display()
p1.printing()
p1.show() 

'''

#Example of Multiple Inheritance and code:
#example 13:
'''
class land_animal:
    def printing(self):
        print("This animal lives on land")
class water_animal:
    def display(self):
        print("This aimal lives in water")

class fog(land_animal,water_animal):
    pass       #here the pass shows that it is empty class means it have no method but in this example due inheritance the fog class get the charcter of land_animal and water_animal
f1=fog()
f1.printing()
f1.display()

'''

#lecture 6 Method of overriding:
#example 6:

'''
class A:
    def display(self):
        print("Method belong to class A")

class B(A):
    pass  #empty class

b1=B()
b1.display()
'''
#Now by using same method but we want diffrent method body in dirived class than we can use the overridding this method 
#in the derived_class not in base_class if forgot what is derived_class and base_class than see basic syntaxt i have written 
#in line number: 107 as writing in code below:

'''
class A:
    def display(self):
        print("Method belong to class A")

class B(A):
    def display(self):
        print("Method belong to class B")

b1=B()
b1.display()
#in simple words overwriting is nothing but it is the ability of class to change the implimentaion of 
# provided by one of its anccestor.  
# OR  We can say that we can change the implementation of method in derived class
#which is provied by the its Base_class.
'''

#lecture 7:
#example 13:
#Encapsulation



#encapsulation:
#Example 13 a.)
'''
class car:
    def __init__(self):
        self.__updatesoftware() #Here the __double underscore is for showing that it is the methode that sart with the
                                # the ubderscore is private method..
    def drive(self):
        print("driving")
    def __updatesoftware(self):  #Here also we write underscore for using the private method
        print("updating software")
blackcar=car()
blackcar.drive()
'''
#car' object has no attribute '__updatesoftware TYPE ERROR FOR SHOWING THIS EXAMPLE IS TAKEN..
#Example 13 b.)
'''
class car:
    # def __init__(self):
        # self.__updatesoftware() #Here the __double underscore is for showing that it is the methode that sart with the
                                # the ubderscore is private method..
    def drive(self):
        print("Hello")
    def __updatesoftware(self):  #Here also we write underscore for using the private method
        print("Jarvis")
p1=car()
p1.__updatesoftware()#car' object has no attribute '__updatesoftware TYPE ERROR FOR SHOWING THIS EXAMPLE IS TAKEN..

'''
#Example 13 c.)
#In this Example :we cannot access private variable outside the class
#output of this:
#driving
#200
#100
'''
class car:
    __maxspeed=0
    __name=" "
    def __init__(self):
        self.__maxspeed=200
        self.__name="supercar"
    def drive(self):
        print("Driving")
        print(self.__maxspeed)
    def setspeed(self,speed):
        self.__maxspeed=speed
        print(self.__maxspeed)
        
redcar=car()
redcar.drive()
redcar.setspeed(100)


'''


#try to modify the private variable outside the class what will happen if we see that below its value is not changing of private variable..

#output of this:
# Driving
# 200
# Driving
# 200
'''
class car:
    __maxspeed=0
    __name=" "
    def __init__(self):
        self.__maxspeed=200
        self.__name="supercar"
    def drive(self):
        print("Driving")
        print(self.__maxspeed)
    # def setspeed(self,speed):
    #     self.__maxspeed=speed
    #     print(self.__maxspeed)
        
redcar=car()
redcar.drive()
redcar.__maxspeed=speed=100   #trying to modify the private variable outside the class in yhis line..
redcar.drive()


'''
# LAST LECTURE:   
# Polymorphism:

#Polymorphism is the ability of an object to take on many forms.
#OR
# It refers to the use of a single type entity (method, operator or object) to represent different types in different scenarios.

# In this example here the plus method is represent 2 different types in different scenario

#Example 1 by harry bhai:
'''
print(5+6)      #here Plus sign is used for adding two integers
print("5"+"6")  #here Plus sign is used for concatenation of two strings

'''
#example by Amuly's: of polymorphism:
'''
class dog:
    def sound(self):
        print("bow bow")
class cat:
    def sound(self):
        print("meow")
def makesound(animaltype):
    animaltype.sound()
catobj=cat()
dogobj=dog()
makesound(catobj)
makesound(dogobj)
'''








