#Data Types 1.Python Numbers
fish = 22
print(fish, "is of type", type(fish))

#fish = "22"
#print(fish, "is of type", type(fish))

weight = 5.05
print(weight, "is of type",  type(weight))

#Data Type 2. Python list
print("Print my list below: §")
mylist =["Digikids", 450, 20, 74.93,"Students"]
print(mylist)

print("Extracting an item from the list")
print ("mylist[1] item is: ", mylist[1])
print ("mylist[0] item is: ", mylist[0])

#show range
print("List range")
mylist = ["Digikids", 450, 20, 74.93,"Students", 56,20,45,"PC", 21]
print("mylist[2:6] is: ", mylist[2:6])

#Data Type 3. Number list
numberlist = ["Numbers", 465, 846, 94, 82, 75, 68, 29, 46, 49, 35, 17, 35, 56, 74, 210,"Teachers"]
print(numberlist)

print("Extracting an item from the list")
print("numberlist[10] item is: ", numberlist[10])
print("numberlist[7] item is: ", numberlist[7])

numberlist[5] = "22"
print(numberlist)

#Data Type 4. Python Tuple
print("These are my tuples: ")
myvar = (14,"Digikds",4.5,"My Class", 57,6.7)
print(myvar)
print("Myvar[3] is:", myvar[3])
#myvar[1] = 10

#Data Type 5. Python Strings
print("This are python strings:")
greetings = "How are you?"
print(greetings)
hello = 'How are you Today? Will you go to swimming in the afternoon?'
print(hello)
#Triple quotes
awesome = """"
How are you?
Have you eaten?
Will you go to swimming
In the afternoon
"""
print(awesome)

good = "How are you?"
print("Extract good[2] is : ", good[5])
print(good[2:8])
#good[1]= 0


#Data Types 6. Python set
print("print the ordered list")
books = {40,34,2,2,6,8,8,8,8,8,40,15, "Digikids", "Digikids", "digikids"}
print(books)
print(type(books))
#set object does not support indexing: print(books[4])


#Data Type 7. Python Dictionary
digikids ={'student':12,'student':8,'student':15, \
    2:'parent'
}
print(digikids[2])
#print(digikids['parent'])
































































