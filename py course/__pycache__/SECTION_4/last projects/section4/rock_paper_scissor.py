import random 

options=["rock","paper","scissor"]
computer_selection=random.choice(options)
player_selection=None
while player_selection not in options:
 player_selection =input("hello player select your weapon")
if player_selection == computer_selection:
 print("tie ! play again")
elif player_selection =="scissor" and computer_selection == "paper":
 print("you win")
elif player_selection =="rock" and computer_selection == "scissor":
 print("you win!")
elif player_selection =="paper" and computer_selection == "rock":
 print("you win!!")
else:
 print("you lose man!")
print(computer_selection)
print(player_selection)