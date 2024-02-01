#Write a program to print the multiplication table of a given number.
#Create a program to find the factorial of a given number using a loop.
#Write a program to print the Fibonacci series up to a specified number of terms.
#Develop a program to determine whether a given number is prime or not.
#Create a program to calculate the sum of digits of a given number.
#Write a program to print the first n natural numbers in reverse order.
#Develop a program to find the sum of all even numbers between 1 and n.
#Create a program to count the number of digits in a given number.
#Write a program to check whether a given number is an Armstrong number or not.
#Develop a program to generate the Pascal's triangle up to a specified number of rows.


num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)



num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("Factorial of", num, "is", factorial)



terms = int(input("Enter the number of terms: "))
a, b = 0, 1
print("Fibonacci series:")
for i in range(terms):
    print(a, end=" ")
    a, b = b, a + b



num = int(input("Enter a number: "))
is_prime = True
if num > 1:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
else:
    is_prime = False
if is_prime:
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")



num = int(input("Enter a number: "))
sum_of_digits = 0
while num > 0:
    digit = num % 10
    sum_of_digits += digit
    num //= 10
print("Sum of digits:", sum_of_digits)



n = int(input("Enter a number: "))
for i in range(n, 0, -1):
    print(i, end=" ")



n = int(input("Enter a number: "))
total = 0
for i in range(2, n + 1, 2):
    total += i
print("Sum of even numbers up to", n, "is", total)



num = int(input("Enter a number: "))
count = 0
while num > 0:
    num //= 10
    count += 1
print("Number of digits:", count)



num = int(input("Enter a number: "))
order = len(str(num))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10
if num == sum:
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")



rows = int(input("Enter the number of rows: "))
for i in range(rows):
    num = 1
    for j in range(rows - i):
        print(" ", end="")
    for k in range(i + 1):
        print(" ", num, sep="", end="")
        num = num * (i - k) // (k + 1)
    print()




