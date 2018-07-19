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