import random

names = ["Luis","Gustavo", "Fernando", "Ola", "Maeve", "Otis"]

score_students = {student:random.randint(1,100) for student in names}

print(f"Resultados= {score_students}")

passed_students = {key:value for (key , value) in score_students.items() if value > 60}

print(f'Alumnos Aprobados = {passed_students}')
