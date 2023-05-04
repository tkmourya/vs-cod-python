f = input("enter first number : ")
operator = input("enter operator (+,-,*,/,%) : ")
s = input("enter second number : ")

f = int(f)
s = int(s)

if operator == "+":
    print(f + s)
elif operator == "-":
    print(f - s)
elif operator == "*":
    print(f * s)
elif operator == "/":
    print(f / s)
elif operator == "%":
    print(f % s)
else:
    print(" invalid operation")