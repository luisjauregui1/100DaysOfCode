# with open("a_file.txt") as file:
#     file.read()
   
#     error en terminal:
#     Traceback (most recent call last):
#     File "c:\Users\Gustavo\Documents\codigo\100DaysOfCode\seccion30\main.py", line 1, in <module>
#     with open("a_file.txt") as file:
#          ~~~~^^^^^^^^^^^^^^
#     FileNotFoundError: [Errno 2] No such file or directory: 'a_file.txt'
    
   
# try: 
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["ashdfoasdfoa"])
    
# except FileNotFoundError: 
#     file = open('a_file.txt', "w")

# except KeyError as error_message:
#     print(f"That key {error_message} does not exist.")

# else: 
#     content = file.read()
# finally:
#     raise TypeError("This is an error that i made up.")

    
height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError

bmi = weight / height ** 2
print(bmi)

    
    