# "Your BMI is 18.28678, you are underweight."
# "Your BMI is 22.0, you have a normal weight."
# "Your BMI is 28.50752, you are slightly overweight."
# "Your BMI is 32.56189, you are obese."
# "Your BMI is 37.50000, you are clinically obese."

# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
body = weight / (height * height)
body_bmi = float("{:.5f}".format(body))

print(type(body_bmi))



if body_bmi < 18.5:
    print(f"Your BMI is {body_bmi}, you are underweight.")
elif 18.5 <= body_bmi < 25:
    print(f"Your BMI is {body_bmi}, you have a normal weight.")
elif 25 <= body_bmi < 30:
    print(f"Your BMI is {body_bmi}, you are slightly overweight.")
elif 30 <= body_bmi < 35:
    print(f"Your BMI is {body_bmi}, you are clinically obese.")
else:
    print(f"Your BMI is {body_bmi}, you are clinically obese.")


"""
Under 18.5 they are underweight
Equal to or over 18.5 but below 25 they have a normal weight
Equal to or over 25 but below 30 they are slightly overweight
Equal to or over 30 but below 35 they are obese
Equal to or over 35 they are clinically obese.
"""