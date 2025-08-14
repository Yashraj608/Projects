import random
#Rock Paper Scissor Game#
print("------Welcome to Rock Paper Scissor Game------")
name = input("Enter your name: ")
Game_list = ["Rock","Paper","Scissor"]
user_input = input("Enter your move----Rock/Paper/Scissor: ").capitalize()
computer_input = random.choice(Game_list)

print(f"{name} chooses {user_input} ")
print(f"Computer chooses {computer_input} ")

if(user_input == computer_input):
    print("It's a tie!....")
elif(user_input =="Rock" and computer_input == "Paper"):
    print("Paper wraps the rocks...so Paper wins")
elif(user_input == "Paper" and computer_input == "Rock"):
    print("Paper wraps the rocks...so Paper wins")
elif(user_input == "Rock" and computer_input == "Scissor"):
    print("Rock breaks the Scissor...so Rock wins")
elif(user_input == "Scissor" and computer_input == "Rock"):
    print("Rock breaks the Scissor...so Rock wins")
elif(user_input == "Scissor" and computer_input == "Paper"):
    print("Scissor is sharp and cuts the paper...so Scissor wins")
elif(user_input == "Paper" and computer_input == "Scissor"):
    print("Scissor is sharp and cuts the paper...so Scissor wins")
else:
    print("Invalid Choice")