# rock paper sicissor game
import time
import random
print("Welcome to Rock , Paper,Scissor game")
time.sleep(1)
list=["r","p","s"]
no_of_chance=6
chances=0
human=0
comp=0
while chances<no_of_chance:
    user= input("Enter r for ROck \n s for Scissor \n p for Paper\n\n")
    bot= random.choice(list)
    if bot==user:
        print("Its draw so no point to each other\n")
        print(f"your guess {user} and computer guess is {bot} \n")
    elif bot=="r" and user=="s":
        comp=comp+1
        print(f"your guess {user} and computer guess is {bot} \n")
        print("You loose comp got 1 point\n")
        print(f"Computer point:{comp} and your point: {human}\n")
    elif bot=="s" and user=="r":
        print(f"your guess {user} and computer guess is {bot} \n")
        print("You got 1 point\n")
        human+=1
        print(f"Computer point:{comp} and your point: {human}")
    elif bot=="r" and user=="p":
        print(f"your guess {user} and computer guess is {bot} \n")
        print("You got one point") 
        human+=1
        print(f"Computer point:{comp} and your point: {human}")
    elif bot=="p" and user=="r":
        print(f"your guess {user} and computer guess is {bot} \n")
        print("Computer got one point") 
        comp+=1
        print(f"Computer point:{comp} and your point: {human}")
    elif bot=="s" and user=="p":
        print(f"your guess {user} and computer guess is {bot} \n")
        print("Computer got one point") 
        comp+=1
        print(f"Computer point:{comp} and your point: {human}")
    elif bot=="p" and user=="s":
        print(f"your guess {user} and computer guess is {bot} \n")
        print("You got one point") 
        human+=1
        print(f"Computer point:{comp} and your point: {human}")
    else :
        print("You have give wrong input\n")
    chances+=1
    print(no_of_chance-chances," chances left")
    print(f"your point upto now{human} and computer point {comp}")
print("Game over")
if human==comp:
    print("Tie")
elif human>comp:
    print(f"You won by {human-comp} point")
else:
    print(f"Computer wins by {comp-human} point")
print(f"Your point is {human} and computer got{comp}")

   

