print("Press 1 to add(+).")
print("Press 2 to subtract(-).")
print("Press 3 to multiply(x).")
print("Press 4 to division(/).")
print("Press 5 to get remainder.")
print("Press 6 to get quotient.")

c = int(input("Select the operation you want to perform : "))
a = int(input("Enter 1st no. : "))
b = int(input("Enter 2nd no. : "))

if c == 1:
    print("Sum of", a, "and", b, "is : ", a + b)
elif c == 2:
    print("Difference of", a, "and", b, "is : ", a - b)
elif c == 3:
    print("Multiplication of", a, "and", b, "is : ", a * b)
elif c == 4:
    print("Division of", a, "and", b, "is : ", a / b)        # / operator is used to return the division value(always returns the value in float)
elif c == 5:
    print("Remainder of", a, "when divided", b, "is : ", a % b)  # % operator is used to return remainder
elif c == 6:
    print("Quotient of", a, "when divided by", b, "is : ", a//b)  # // operator is used to print quotient

print("Thank You! Happy Learning.")
