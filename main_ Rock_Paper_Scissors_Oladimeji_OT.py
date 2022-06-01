#python
#python

import random

#print("I will not drop out of this program\nI will finish and finish well")

#Name = input("Hi, enter your name: ")
#print("Hi " +Name+ ",you want to play rock, paper scissors\n here we goooo")

while True:
    play_choices = ["Rock", "Paper", "Scissors"]
    #print(play_choices)

    #while(Player==CPU):
    Player = input("Select an option from the List: 'Rock', 'Paper', 'Scissors': ")
    CPU = random.choice(play_choices)
    Player = Player.capitalize()
    CPU = CPU.capitalize()
    print("Player(" +Player+ "):","CPU(" +CPU+ ")")


    if((Player not in play_choices) | (CPU not in play_choices)):
        print("Error!!!, Try again...")
        Player = input("Select an option from the List: 'Rock', 'Paper', 'Scissors': ")
        CPU = random.choice(play_choices)
        print("Player(" +Player+ "):","CPU(" +CPU+ ")")
    elif(((Player=="Rock")and(CPU =="Scissors"))|((Player=="Paper")and(CPU =="Rock"))|((Player=="Scissors")and(CPU =="Paper"))):
        print("Player wins")
    elif(((CPU=="Rock")and(Player =="Scissors"))|((CPU=="Paper")and(Player =="Rock"))|((CPU=="Scissors")and(Player =="Paper"))):
        print("CPU wins")
    else:
        play_again = input("Play again? (y/n): ")
        if play_again.lower() !="y":
            break

    


#if choices =="R"|"r":
