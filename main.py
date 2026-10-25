





import random

def swg():
    computer = random.choice(['Snake','Water','Gun'])
    player = input("Choose Snake, Water or Gun : ").title()

    print(f"You chose :{player}\nComputer chose: {computer}")

    if player == computer:
        print("It's a draw!")
    elif ((player == 'Snake'and computer =='Water')or 
          (player == 'Water' and computer== 'Gun')or
          (player == 'Gun' and computer == 'Snake')
          ):
        print("Player wins")

    elif player in ['Snake','Water','Gun']:
        print("Computer wins")
    else:
        print("Invalid Choice of the player!")

swg()



