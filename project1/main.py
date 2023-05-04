import random
# snake water gun (GAME)

def gamewin(computer, you):
    # if two value are equal, declare a tie!
    if computer == you:
        return None

    # check for all possiblities when computer chose s
    elif computer == 's':
        if you == 'w':
         return False
    elif you == 'g':
        return True

     # check for all possiblities when computer chose w
    elif computer == 'w':
        if you == 'g':
            return False
    elif you == 's':
            return True

     # check for all possiblities when computer chose g
    elif computer == 'g':
        if you == 's':
            return False
    elif you == 'w':
            return True



print("computer turn: snake(s) water(w) or gun(g)?")
randno = random. randint(1, 3)
if randno == 1:
    computer = 's'
elif randno == 2:
    computer = 'w'
elif randno == 3:
    computer = 'g'

you = input("your turn: sanke(s) water(w) or gun(g)?")
a = gamewin(computer, you)
print(f"computer chose {computer}")
print(f"you chose {you}")

if a == None:
    print("the game is a tie!")
elif a:
    print("you win!")
else:
    print("you lose!")



