#rock paper scissor game
import random
user_choice=int(input("enter your choice:type 0 for Rock,type 1 for paper,type 2 for scissor"))
if user_choice>=3 or user_choice<0:
    print("you enetered invalid choice,you loose")
else:
    computer_choice=random.randint(0,2)
print("computer choose")
print(computer_choice)
if computer_choice==user_choice:
    print("it's draw")
elif computer_choice==0 and user_choice==2:
    print("you loose")
elif user_choice==0 and computer_choice==2:
    print("you win")
elif computer_choice>user_choice:
    print("you loose")
elif user_choice>computer_choice:
    print("you win")
