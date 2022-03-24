from tokenize import group


print("List iteration")
myclass = ["Digikids", "for", "Coders"]
for i in myclass:
    print(i)

numbers = [2,5,1,4,6,8]
for i in numbers:
    print(numbers)

# Iterating over a Tuple
print("Tuple iteration")
mytuple = ("Digikids", "for", "Coders")
for i in mytuple:
    print(i)

print("Today\nis\nThursday")
print("TodayisThursday")
print("Today is Thursday")
print("Today\tis\tThursday")

#Iterating over a string
print("\nString Iterations")
mystring = "Hello Digikids"
for i in mystring:
    print(i)

#Iterating a string
print("\nString Iterations")
mypc = "Nairobi city"
for i in mypc:
    print(i)

#Python Range() function
for value in range(4):
    print(value)

print("\range in 1")
for elfu in range(1):
    print(elfu)

print("\range in 9")
for elfu in range(9):
    print(elfu)

print("\range in 8")
for elfu in range(8):
    print(elfu)


#nested loops
print("\nested grups")
number = ['5', '8', '10']
colours = ['red', 'blue', 'black']
for a in number:
    for z in colours:
        print(a,z)

#else in for loop
print("\nelse in for loop")
for value in range(5):
    print(value)
else:
    print("End of loops")

#For loop backward
print("\nShowing the for loop backward")
for val in reversed(range(5)):
    print(val)

#else in for loop
print("\nelse in for loop")
for tin in range(51):
    print(tin)
else:
    print("End of loops")

#For loop backward
print("\nShowing the for loop backward")
for type in reversed(range(101)):
    print(type)




    
