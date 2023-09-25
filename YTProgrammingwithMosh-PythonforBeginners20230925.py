print("Hello World")

name = input("What is your name? ")
print("Hello " + name)

age = 2023 - int(input("Enter your birth year and I will calculate your age: "))
print("You are " + str(age) + " years old.")
if age < 20:
    print("Wow you're very young!")
elif age > 50:
    print("Nice, you still have plenty of life still in you")
else:
    print("You're in your prime time ;)")

response = "Y"
while response == "Y":
    weight = float(input("What is your weight? "))
    unit = input("Did you input your weight in (K)g or (L)bs? ")
    if unit.upper() == "K":
        print("Did you know that is " + str(weight*2.205) + " pounds (lbs)?")
    elif unit.upper() == "L":
        print("Did you know that is " + str(weight/2.205) + " kilograms (kg)?")
    response = input("Did you want to try with a different number (Y/N)? ")
    if response.upper() == "N":
        print("No worries~")
        response = response.upper()
    elif response.upper() == "Y":
        response = response.upper()
