a = 10 #The above is expression

print("The value of a is ",a) #This is statement

#The Comment always starts with Hash symbol in Python

#The function is defined below
def U():
    print("This is function")

U()

#The below is identation and code block
if a < 9:
    print("a is greater than 9") #This is indentation
else:
    print("a is less than or equal to 9")

#Check the string that it is keyword or not
import keyword
print(keyword.kwlist)

word = ["word","for", "if", "no", "none"]
for i in range(len(word)):
    if(keyword.iskeyword(word[i])):
        print(word[i], "is a keyword.")
    else:
        print(word[i], "is not a keyword.")

#Print without new line
print("Umar", end=" ")
print("Farooq")

#Calculator
import os 
num1 = int(input("Enter First Number:"))
num2 = int(input("Enter Second Number:"))
print("For Addition Type add")
print("For Subtraction, type sub")
print("For Multiplication, type mul")
print("For Division, type div")
opr = input("Enter the arithematic opeartion:")
if opr == "add":
    print(num1 + num2)
if opr == "sub":
    print(num1 - num2)
if opr == "mul":
    print(num1 * num2)
if opr == "div":
    print(num1 / num2)

