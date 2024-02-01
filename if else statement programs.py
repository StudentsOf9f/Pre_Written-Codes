#Write a program to check whether a given number is even or odd.
#write a program to find the largest among three numbers entered by the user.
#Develop a program to determine whether a given year is a leap year or not.
#Create a program to classify a given triangle (scalene, isosceles, or equilateral) based on the lengths of its sides.
#Write a program to determine whether a character entered by the user is a vowel or a consonant.
#Create a program to calculate the electricity bill for a user. The program should take the number of units consumed as input and apply appropriate charges based on predefined slab rates (e.g., first 100 units at Rs. 5 per unit, next 200 units at Rs. 7 per unit, and so on).
#Develop a program to determine whether a given number is positive, negative, or zero.
#Write a program to determine the eligibility of a candidate for voting. The program should ask for the age of the user and determine whether they are eligible to vote based on the legal voting age (e.g., 18 years and above).
#Create a program to determine the roots of a quadratic equation. The program should take coefficients as input and display the roots accordingly, considering cases for real and imaginary roots.
 
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")



marks = float(input("Enter your marks: "))
if marks >= 40:
    print("Congratulations! You have passed.")
else:
    print("Sorry! You have failed.")



num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
if num1 >= num2 and num1 >= num3:
    print(num1, "is the largest number.")
elif num2 >= num1 and num2 >= num3:
    print(num2, "is the largest number.")
else:
    print(num3, "is the largest number.")




year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")




side1 = int(input("Enter length of first side: "))
side2 = int(input("Enter length of second side: "))
side3 = int(input("Enter length of third side: "))
if side1 == side2 == side3:
    print("Equilateral triangle")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("Isosceles triangle")
else:
    print("Scalene triangle")




char = input("Enter a character: ")
if char.lower() in ['a', 'e', 'i', 'o', 'u']:
    print(char, "is a vowel.")
else:
    print(char, "is a consonant.")




units = int(input("Enter units consumed: "))
if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = 100 * 5 + (units - 100) * 7
# Add more conditions for different slabs
print("Electricity bill: Rs.", bill)



num = float(input("Enter a number: "))
if num > 0:
    print("Positive number.")
elif num < 0:
    print("Negative number.")
else:
    print("Zero.")




age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")





