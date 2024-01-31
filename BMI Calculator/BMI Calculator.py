print("BMI stands for Body Mass Index")

response = "Y"
while response.upper() == "Y":
    height = float(input("To calculate your BMI, please enter your height in metres (m): "))
    weight = float(input("Please enter your weight in kilograms (kg): "))
    BMI = weight / (height * height)
    ideal_lowest_weight = 18.5 * (height * height)
    ideal_highest_weight = 24.99 * (height * height)
    print(f'Your BMI is {BMI}')
    if BMI < 18.5:
        weight_status = "underweight"
    elif 18.5 <= BMI < 25:
        weight_status = "at a healthy weight"
    elif 25 <= BMI < 30.0:
        weight_status = "overweight"
    else:
        weight_status = "obese"
    print(f'You are {weight_status} for your height.'
          f'The ideal weight for your height is between {ideal_lowest_weight} and {ideal_highest_weight}')
    response = input("Did you want to try with a different number (Y/N)? ")
