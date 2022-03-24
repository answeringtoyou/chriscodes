count = int(input("Enter the count of number: "))
i = 0
sum = 0
for i in range(count):
    x = int(input("Enter an interger: "))
    sum = sum + x
avg = sum/count
print(" The average is: ", avg)