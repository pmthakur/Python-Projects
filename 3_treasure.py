print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your Mission is to find the treasure.")
choice1 = input('you are at a crossroad, Where do you want to go? Type "Left" or "Right".').lower()

if choice1 == "left":
    choice2 = input('you ae come to a lake.their is an island in the middle of the lake. type "wait" for a boat. Type "swim" to swim across.\n').lower()
    if choice2 == "wait":
        choice3 = input("you arrives at island unharmed. their is house with three door. one red. one yellow. one blue, which color do you choose?\n").lower()
        if choice3 == "red":
            print("It's Room full of fire. Game Over")
        elif choice3 == "Yellow":
            print("you find the treasure. you win!")
        elif choice3 == "blue":
            print("You entered a room of beast. Game Over.")
        else:
            print("you choose a door that does't exist. Game Over.")
    else:
        print("You attacked by an angry trout. Game Over.")
else:
        print("You fell into a hole. Game Over.")
