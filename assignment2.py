name = input("Enter your name: ")
age = int(input("Enter your age: "))
gpa = float(input("Enter your GPA: "))
graduated = input("Have you graduated? (yes/no): ")

print(f"\nHello, {name}!")
print("Age:", age)
print("GPA:", gpa)
print("Graduated:", graduated, "\n")
print("Analyzing your data...\n")

if age < 25 and gpa >= 3.5 and graduated.lower() == "yes":
    print("result: You are eligible for the scholarship!\n")
elif age < 30 and gpa >= 2.5 and graduated.lower() == "no":
    print("result: You are eligible for the internship program!\n")
else:
    print("result: You are not eligible, please try again later.\n")