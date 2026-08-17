import random

choices = ["Snake","Water","Gun"]
user = input("Enter Snake, Water or Gun:")

computer = random.choice(choices)

print("You Chose :",user) 
print("Computer Chose :",computer)

if(user== computer):
    print("Match Draw!!!")
elif(user =="Snake" and computer=="Water" or user == "Water" and computer == "Gun" or user == "Gun" and computer == "Snake"):
    print("User Won")
else:
    print("Computer Won")


                        #  OR 


import random

choices = ["snake", "water", "gun"]

user = input("Enter snake, water or gun: ")

computer = random.choice(choices)

print("You chose:", user)
print("Computer chose:", computer)

if user == computer:
    print("Match Draw!")

elif (user == "snake" and computer == "water") or \
     (user == "water" and computer == "gun") or \
     (user == "gun" and computer == "snake"):
    print("You Win!")

else:
    print("Computer Wins!")


