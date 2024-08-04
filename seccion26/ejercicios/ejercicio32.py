"""
You are going to use Dictionary Comprehension to create a dictionary called weather_f that takes each temperature in degrees Celsius and converts it into degrees Fahrenheit.

To convert temp_c into temp_f use this formula:

(temp_c * 9/5) + 32 = temp_f

"""

weather_c = eval(input())
# 🚨 Don't change code above 👆


# Write your code 👇 below:
weather_f = {valor:(clave * 9/5 + 32) for (valor, clave) in weather_c.items() }

print(weather_f)