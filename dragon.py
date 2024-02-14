2import random
import time
def displayIntro() :
    print('you are in a land full of dragons.')
    print('you see two caves. In one cave, the dragon is friendly')
    print('and will share his treasure with you. The other')
    print('is greedy and hungry, and will eat you on sight.')
    print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave will you go into? (1 or 2)')
        cave = input()

    return cave

def checkCave(chosenCave):
    print('you approac the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! ')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print('Gives you his treasure!')
    else:
        print('Gobbles you down in one bite!')

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':

    displayIntro()

    caveNumber = chooseCave()

    checkCave(caveNumber)

    print('Do you want to play again? (yes or no)')
    playAgain = input()
