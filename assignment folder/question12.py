from unicodedata import digit


sum = 0
number = int(input("Enter an interger: "))
while(number!=0):
    digit = number%10
    sum = sum+digit
    number = number//10
print("Sum of digit is: ", sum)
