"""PYTHON """
# a = "Hello World"
# print(a.replace('H', 'J' ))

"""split mehtod"""
# a = "hello World"
# print(a.split(","))

"""user input"""
# print("Enter your name:")
# x = input()
# print(" Hello " +x)

"""Addition of two no """
# print("Addition of two variable")
#
# num1 = float(input("Please Enter first number : "))
# num2 = float(input("Please Enter secound number :"))
# sum = float(num1) + float(num2)
# print('The total of :',sum)

"""Change list"""
# list = ['Apple', 'Banana', 'Cherry']
# list[2] = 'Mango'
# print(list)

"""Constructor under list"""
# thislist = list(('apple','banana','mango')) #note double bracket use constructor
# print(thislist)


"""using append() mehtod to add list item"""
# thislist = list(('Linux','Windows','Unix'))
# thislist.append('My love is MAC')
# print(thislist)

"""using remove() method to remove item into list"""

# thislist = list(('Linux','Windows','My First Love Mac'))
# # thislist.remove(thislist[1])
# # print(thislist)


"""using len() method to to see length of  list"""

# thislist = list(('Linux','Windows','Apple'))
# thislist=(len(thislist))
# print(thislist)


# Python all method and description dude
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list

"""using sorted list"""
# thislist = list(('Windows','Linux','Apple'))
# thislist = (sorted(thislist))
# print(thislist)


"""Tuple is collection of ordered but Tuple is unchangable & Tuple  is wrriten into round bracket
Tuple is similar to list
"""
# thisTuple = ('Windows','My love MacOs Sierra','Linux')
# print(thisTuple)

"""You canot change Tuple"""
# thisTuple = ('Windows','My love MacOs Sierra','Linux')
# thisTuple[3]='Unix' #test changabilitly
# print(thisTuple)


""" using Tuple Constructor use (()) bracket"""
# thisTuple = tuple (('Windows','My Love MACOS Sierra','Linux'))
# print(thisTuple)

"""using Tuple constructor lenth of tuple"""
# thisTuple = tuple(('Windows','My Love MacOs Sierra','Unix'))
# thisTuple=(len(thisTuple))
# print(thisTuple)



"""Set is collection of unordered and unindexed. In python set is are written in python curly brackets"""

# thisSet = {'Windows','Mac','Linux'}
# print(thisSet)
#the set list is unordered, so the items will appear in a random order.


"""Set() using constructor"""
# thisSet = (('windows','Mac','Linux'))
# print(thisSet)

"""using add() mehtod Set"""
# thisSet = set(('Windows','Mac','Linux','unix'))
# thisSet.add('Apple dude')
# print(thisSet)

"""Set using remove() method"""
# thisSet = set(('Windows','Mac','Ubantu','linux'))
# thisSet.remove('Ubantu')
# print(thisSet)
#

"""Set using len() method"""
# thisSet = set(('windows','apple','unix','linux'))
# print(len(thisSet))


"""Dictionary :-A dictionary is a collection which is unordered, changeable and indexed.
 In Python dictionaries are written with curly brackets, and they have keys and values."""

# thisDict = {
#     'Apple' : 'Steve Job',
#     'Windows': 'Bill Gates',
#     'Linux' : 'linus Tordvals'
# }
# print(thisDict)


""" Set use dict() construcotr"""
# thisDict =dict(Apple='SteveJobs',Windows='Bill Gates',Linux='linus tordvals')
# print(thisDict)

"""Adding item dictonary"""
# thisDict = dict(Apple='SteveJobs',Windows='Bill Gates',Linux='linus tordvals')
# thisDict['facebook']= 'Mark Zukerbug'
# print(thisDict)


"""Removee item dictionary using del()method"""
# thisDict =dict(Apple='SteveJobs',Windows='Bill Gates',Linux='linus tordvals')
# del(thisDict['Windows'])
# print(thisDict)


"""Python Condition and if statement"""
# x = 500
# y = 600
# if y >  x:
#     print("y is  gretter than x")

"""Else if statemetn"""
# x = 600
# y = 600
# if(x > y):
#     print("x is greater than y")
# elif(x == y):
#     print("x is equal to y")


"""Else Statement"""
# x = 600
# y = 700
# if(x > y):
#     print("x is greater than y")
# elif(x == y):
#     print("x is equal to y")
# else:
#     print("y is greater than x")



""" While Loops """
"""While loop we can execute a set of statements as long as a condition is true"""

# i = 1
# while i < 6:
#     print(i)
#     i += 1

"""Break statement """
# i = 1
# while i < 6:
#   print(i)
#   if i == 3:
#     break
#   i += 1

"""Continue statement"""
# i = 0
# while i < 6:
#   i += 1
#   if i == 3:
#     continue
#   print(i)


"""For Loop"""
"""A for loop is used for iterating over a sequence (that is either a list, a tuple or a string)"""
"""for loop we can execute a set of statements, once for each item in a list, tuple, set etc."""
"""The for loop does not require an indexing variable to set beforehand, as the for command itself allows for this."""
# fruits = ['apple','orange','mango']
# for x in fruits:
#     print(fruits)

"""Break statement for loop"""
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     break
#   print(x)


"""For loop Continue statement"""
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     continue
#   print(x)

"""For loop range()function"""
# for x in range(2,10):
#     print(x)

"""The range() function defaults to increment the sequence by 1, 
however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3)"""
# for x in range (2,20,3):
#     print(x)


"""Recursion is a common mathematical and programming concept. It means that a function calls itself. 
This has the benefit of meaning that you can loop through data to reach a result."""
# def tri_recursion(k):
#   if(k>0):
#     result = k+tri_recursion(k-1)
#     print(result)
#   else:
#     result = 0
#   return result
#
# print("\n\nRecursion Example Results")
# tri_recursion(6)


"""Python in Function """
"""Function is block of code which run only its call
You can pass data known parameter into function. function its return dataa  as result"""
"""Python function declare def keyword"""

# def my_function() -> object:
#   print('Hello dude you are learn python!')
#
# my_function()

"""Parameter python """
"""Information can passed as parameter function. parameter are specified function name under"""
# def my_function(fname):
#   print(fname + " patil")
#
# my_function("Rahul")
# my_function("Rohan")
# my_function("Arnav")


"""Default parameter"""
# def my_function(country: object = "India") -> object:
#   print("I am from " + country)
#
# my_function("Sweden")
# my_function("Iceland")
# my_function()
# my_function("Brazil")

"""Return value """

# def  my_function(x):
#     return 5 * x
# print(my_function(10))
# print(my_function(1000))


"""Lamda function """
"""lambda function is use  python to declare anonymous function"""

# myfunc = lambda i:i * 2
# print(myfunc(14))

# myfunc = lambda x,y: x*y
# print(myfunc(3,6))

"""The power of lambda is better shown when you generate anonymous functions at run-time"""
#
# def myfunc(n):
#   return lambda i: i*n
#
# doubler = myfunc(2)
# tripler = myfunc(3)
# val = 11
# print("Doubled: " + str(doubler(val)) + ". Tripled: " + str(tripler(val)))

""" Python Array """
"""Array are stored multiple value in one single variable"""

# cars = ['BMW','Volvo','Ford','Volvo','Tesla']
# x = cars[4]
# print(x)

"""Modify the value"""
# cars = ["Ford", "Volvo", "BMW"]
#
# cars[0] = "Toyota"
#
# print(cars)

"""Lenth of cars"""
# cars = ["Ford", "Volvo", "BMW"]
#
# x = len(cars)
#
# print(x)

"""for in array"""
# cars = ["Ford", "Volvo", "BMW"]
# for x in cars:
#     print(x)


"""append()in array"""
# cars = ["Ford", "Volvo", "BMW"]
# cars.append('Audi')
# print(cars)


"""remove() element in array using pop()"""
# cars = ["Ford", "Volvo", "BMW"]
# cars.pop(1)
# print(cars)

# Array Methods
# Python has a set of built-in methods that you can use on lists/arrays.
#
# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	    Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list


"""Python Class/Object"""
# Python is an object oriented programming language.
# Almost everything in Python is an object, with its properties and methods.
# A Class is like an object constructor, or a "blueprint" for creating objects.

"""Create object"""
# class MyClass:
#   x = 5
#
# p1 = MyClass()
# print(p1.x)
#

"""__init__ ()Function"""
"""All classes have a function called __init__(), which is always executed when the class is being initiated."""
# The __init__() function is called automatically every time the class is being used to create a new object.

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
# p1 = Person("John", 36)
#
# print(p1.name)
# print(p1.age)


"""Object Method. Method in function"""
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
#   def myfunc(self):
#     print("Hello my name is " + self.name + "and" + "my age is" + self.age)
#
# p1 = Person("Rahul", "22")
# p1.myfunc()

"""Self Parameter"""
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
#   def myfunc(abc):
#     print("Hello my name is " + abc.name)
#
# p1 = Person("Rahul", 22)
# p1.myfunc()

"""Modify Object properties"""

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
#   def myfunc(self):
#     print("Hello my name is " + self.name)
#
# p1 = Person("Rahul", 21)
#
# p1.age = 22
#
# print(p1.age)


"""You can delete object by using del keyword"""
#
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
#   def myfunc(self):
#     print("Hello my name is " + self.name)
#
# p1 = Person("John", 36)
#
# del p1.age
#
# print(p1.age)

"""Module in Python"""
"""Module same as code of library. A file containing a set of functions you want to include in your application."""

# import mymodule
#
# mymodule.greeting('Rahul')

"""Variable in module"""
# import  mymodule
#
# a = mymodule.person1["name"]
# print(a)

"""Naming and Re-naming in module"""
# import mymodule as mx
#
# a = mx.person1=['age']
# print(a)


"""Built in modules"""
#import platform is module

# import platform
#
# x = platform.system()
# print(x)


"""Using dir() function """
"""The dir() function can be used on all modules, also the ones you create yourself"""
# import  platform
#
# x = dir(platform)
# print(x)


"""Import from module"""

# from mymodule import person1
#
# print (person1["country"])


"""Python datetime """
# import datetime
#
# x = datetime.datetime.now()
# print(x)


"""Create date object"""
"""To create a date, we can use the datetime() class (constructor) of the datetime module."""

# import  datetime
#
# x =datetime.datetime(2022,11,12)
#
# print(x)

"""strftime() method """

# import datetime
#
# x = datetime.datetime(2018, 6, 1)
#
# print(x.strftime("%B"))


# A reference of all the legal format codes:
#
# Directive	Description	Example	Try it
# %a	Weekday, short version	Wed
# %A	Weekday, full version	Wednesday
# %w	Weekday as a number 0-6, 0 is Sunday	3
# %d	Day of month 01-31	31
# %b	Month name, short version	Dec
# %B	Month name, full version	December
# %m	Month as a number 01-12	12
# %y	Year, short version, without century	18
# %Y	Year, full version	2018
# %H	Hour 00-23	17
# %I	Hour 00-12	05
# %p	AM/PM	PM
# %M	Minute 00-59	41
# %S	Second 00-59	08
# %f	Microsecond 000000-999999	548513
# %z	UTC offset	+0100
# %Z	Timezone	CST
# %j	Day number of year 001-366	365
# %U	Week number of year, Sunday as the first day of week, 00-53	52
# %W	Week number of year, Monday as the first day of week, 00-53	52
# %c	Local version of date and time	Mon Dec 31 17:41:00 2018
# %x	Local version of date	12/31/18
# %X	Local version of time	17:41:00
# %%	A % character	%


"""Python PIP """
"""A package contains all the files you need for a module.
Modules are Python code libraries you can include in your project."""

# import  camelcase
#
# c = camelcase.CamelCase()
#
# txt = "Rahul done basic python programming"
# 
# print(c.hump(txt))
#
