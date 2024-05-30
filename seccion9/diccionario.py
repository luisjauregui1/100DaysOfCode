# Diccionarios

dic = {"Bug": "An error in a program that prevents the program from running as expected.",
       "Fuction": "A pieace of code that you can easily call over and over agin."}


print(dic["Fuction"])

# adding new items to dictionary.
dic["Loop"] = "The action of doing something over and over again"

# loop through a dictionary
for thing in dic:
    print(thing)
    print(dic[thing])

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆
# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇

for key in student_scores:
    if 91 <= student_scores[key] <= 100:
        student_grades[key] = "Outstanding"
    elif 81 <= student_scores[key] <= 90:
        student_grades[key] = "Exceeds Expectations"
    elif 71 <= student_scores[key] <= 80:
        student_grades[key] = "Acceptable"
    elif student_scores[key] <= 70:
        student_grades[key] = "Fail"


# 🚨 Don't change the code below 👇
print(student_grades)


travel_log = {
    "France":  {"cities_visited": ["paris", "lille", "dijon"], "total_visits": 12},
    "Germany":  {"cities_visited":  ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 4}
}

# Nesting Dictionary in a list
travel_log = [
    {
        "contry": "France",
        "cities_visited": ["paris", "lille", "dijon"],
        "total_visits": 12
    },
    {
        "contry": "Germany", 
        "cities_visited":  ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 4
    }
]

