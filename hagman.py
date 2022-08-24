import random

list = ["dog", "cat", "crab"]

#Defining bord
board = ["0", "0", "0"
         "0", "0", "0",
        "0", "0", "0"]

#Printing board
print("This is the gameboard.")
def print_board():
    print(board[0] + "  " + board[1] + "  " + board[3])
    print(board[3] + "  " + board[4] + "  " + board[5])
    print(board[6] + "  " + board[7] + "  " + board[6])

#Points
user_points = 0

#Alphabet
print_board()
print("Choose from letters a b c d e g i j k l m n o p z")

#print
print("You have 4 attempts.")

#Randomising word
num = random.randint(0, 2)

choosen_word = list[num]

#Lenght of the word
lenght = len(choosen_word)
print("Lenght of the word is " + str(lenght))

#Splitting word
splitWord = []

for letter in choosen_word:
    splitWord.append(letter)

#User input1
user_input1 = input("Please input letter. ")

#If satement 1
if user_input1 in splitWord:
    print(user_input1 + " is in the word.")
    print(user_input1)
else:
    print(user_input1 + " is not in the word")
    user_points = user_points + 1

if user_points == 1:
    print("______")

#User input2
user_input2 = input("Please another input letter. ")

#If statement 2
if user_input2 in splitWord:
    print("You found the letter")
    print(user_input2)
else:
    print(user_input2 + " is not in the word")
    user_points = user_points + 1

if user_points == 2:
    print("      \n   /  \n__/___")

if user_points == 1:
    print("______")

#User input3
user_input3 = input("Please another input letter. ")

#If statement 3
if user_input3 in splitWord:
    print("You found the letter")
    print(user_input3)
else:
    print(user_input3 + " is not in the word")
    user_points = user_points + 1

if user_points == 3:
    print("    __\n   /  \n__/___")

if user_points == 2:
    print("      \n   /  \n__/___")

if user_points == 1:
    print("______")

#User input3
user_input4 = input("Please another input letter. ")

#If statement 4
if user_input4 in splitWord:
    print("You found the letter")
    print(user_input4)
else:
    print(user_input4 + " is not in the word")
    user_points = user_points + 1

if user_points == 4:
    print("    __\n   / *\n__/___")
    print("You died...")
    quit

if user_points == 3:
    print("    __\n   /  \n__/___")

if user_points == 2:
    print("      \n   /  \n__/___")

if user_points == 1:
    print("______")

#End 
ask = input("Do you know the word? ")

if ask == choosen_word:
    print("Great, you found the word!")
else:
    print("No, this is not it, better luck next time. :-)")