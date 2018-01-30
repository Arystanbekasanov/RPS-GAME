#Rock,paper and scissors.
#Guys u menya vse nice!
import random

computer=random.randint(1,3)
print('Welcome to Rock, Paper Scissors! Pick 1 for Rock, 2 for Paper and 3 for Scissors. \n Rock beats Scissors. Scissors cuts Paper and Paper covers Rock. Got it Lets play')
username = input("What is your name? ")
while True:
    Rock = '1 🤜🏻'
    Paper = '2 ✋🏻'
    Scissors = '3 ✌️'
    player=int(input('Please enter number \n1 = Rock, \n2 = Paper, \n3 = Scissors: '))

    if player<1 or player>3:
        player=int(input('Invalid number. Please enter number 1 = Rock, 2 = Paper, 3 = Scissors: '))
    if player<1 or player>3:
        print('Well, type correct numbers please.')
    elif player==4:
        print('Remember Rock = 1, Paper = 2 and Scissors = 3')
    if player==1 and computer==2 or player==2 and computer==3 or player==3 and computer==1:
        print('Computer wins! You lose. 😞 Booo. =(')
    elif computer==2:
        print("Computer chose Paper ")
    elif computer==1:
        print("Computer chose Rock")
    elif computer==3:
        print("Computer chose Scissors")

    if player==1 and computer==1 or player==2 and computer==2 or player==3 and computer==3:
        print("It's draw 🤙")


    if player==1 and computer==3 or player==2 and computer==1 or player==3 and computer==2:
        print('You  won. Well done 🎉 BOB')
        print("Computer chose Scissors")
