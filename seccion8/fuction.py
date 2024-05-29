import math

def paint_calc(height , width, cover):
    number_of_cans = (height * width) / cover
    print(f"You'll need {math.ceil(number_of_cans)} cans of paint.") 


def prime_checker(number):
                
    if number <= 1:
        return False
    
    if number <= 3:
        return True
    
    if number % 2 == 0 or number % 3 == 0:
        return False

    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i = i + 6
    return True


with open("primes.txt", "w") as file:
    for index in range(1, 101):
        if prime_checker(index):
            file.write(f"{index} es primo\n")


