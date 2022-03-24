def BMI(height, weight):
    bmi = weight / (height/100)** 2
    return bmi
weight=float(input("Enter the weight:"))
height=float(input("Enter the height:"))
bmi = BMI(height, weight)
print("The BMI is",bmi, "so ", end='')
if (bmi < 18.5):
    print("underweight")
elif (bmi >= 18.5 and bmi < 24.9):
    print("Healthy")
elif (bmi >= 24.9 and bmi < 30):
    print("overweight")
elif (bmi >= 30):
    print("Obesity")