print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You are at the cross road. where do you want to go ?")
direction = str(input("Type \"left\" or \"right\" "))

if direction == "left":
    print("you have come to a lake. There is an Island in the middle of the lake.")
    direction = str(input("Type \"Wait\" or \"swim\" "))
    if direction == "wait":
        direction = str(input("Type \"red\" or \"yellow\" or \"blue\" "))
        if direction=="red": 
            print("Burned by fire. Game Over.")
        elif direction=="yellow":
             print("You Win!")
        elif direction=="blue":
            print("Eaten by beasts. Game Over.")
        else:
            print("game over")
    else:
        print("Attacked by trout. Game Over.")
else:
    print("Fall into a hole. Game Over.")













'''print("welcome to pizza python deliveries")
size = str(input("enter the size of pizza that you wan S,M,or L"))
pepperoni= str(input("Do you want pepperoni on your pizza ? Y/N?"))
extra_cheese= str(input("do you want extra cheese ? Y/N"))

bill = 0
if size == "S" :
     bill = 15
     if pepperoni == "Y":
        bill +=2
     print("our bill is ${bill}")
     if extra_cheese =="Y":

     print("our bill is ${bill}")

elif size == "M" :
    bill = 20
    print("our bill is ${bill}")
elif size =="L":
    bill = 55
    print("our bill is ${bill}")

'''