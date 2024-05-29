# line1 = ["⬜️", "️⬜️", "️⬜️"]
# line2 = ["⬜️", "⬜️", "️⬜️"]
# line3 = ["⬜️️", "⬜️️", "⬜️️"]
# map = [line1, line2, line3]
# print("Hiding your treasure! X marks the spot.")
# position = input().upper()  # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
# split_position = ','.join(position)


# if split_position[2] == "1":
#     if split_position[0] == "A":
#         map[0][0] = "X"
#     elif split_position[0] == "B":
#         map[0][1] = "X"
#     elif split_position[0] == "C":
#         map[0][2] = "X"

# elif split_position[2] == "2":
#     if split_position[0] == "A":
#         map[1][0] = "X"
#     elif split_position[0] == "B":
#         map[1][1] = "X"
#     elif split_position[0] == "C":
#         map[1][2] = "X"

# elif split_position[2] == "3":
#     if split_position[0] == "A":
#         map[2][0] = "X"
#     elif split_position[0] == "B":
#         map[2][1] = "X"
#     elif split_position[0] == "C":
#         map[2][3] = "X"

# else:
#     print("Does not exists that value!")




# Write your code above this row 👆
# 🚨 Don't change the code below 👇
# print(f"{line1}\n{line2}\n{line3}")

# Mi code 👆 
# Dr Angela code 👇

line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# Your code below
letter = position[0].lower()
abc = ["a", "b", "c"]
letter_index = abc.index(letter)
number_index = int(position[1]) - 1
map[number_index][letter_index] = "X"

print(f"{line1}\n{line2}\n{line3}")