print("Welcome to python pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

#work out how much they need to pay based on their size choise.
bill = 0
if size == "S":
    bill =+ 15
elif size == "M":
    bill =+ 20
elif size == "L":
    bill =+ 25
else:
    print("You typed the wrong inputs.")

#work out how much to add to their bill based on their pepperoni choice.    
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

#work out their final amount based on whatever if they want extra chees.
if extra_cheese == "Y":
    bill += 1
print(f"Your final bill is: {bill}.")
        
