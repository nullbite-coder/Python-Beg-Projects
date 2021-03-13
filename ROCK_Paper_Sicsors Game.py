import random
def comp_choose():
    elem = ['r','p','s']
    comp = random.choice(elem)
    return comp

def winner_check(comp,user):
    if(comp.lower() == user.lower()):
        print("Tie")
        return

    if(comp.lower() =='r' and user.lower() == 's'):
        print("Computer Won")
        return

    if(comp.lower() =='s' and user.lower() == 'p'):
        print("Computer Won")
        return

    if(comp.lower() =='p' and user.lower() == 'r'):
        print("Computer Won")
        return

    else:
        print("You Won")

def game_start():
    choice = 'y'
    while choice == 'y':
        
        print("Hello and Welcome To Rock, Paper Sicsor Game\n")
        comp_choice= comp_choose()
        user_choice = input("Lets Start the game - Choose [R]ock, [P]aper or [S]icsor\n")
        try:
            if(user_choice.lower()=='r' or user_choice.lower()=='p' or user_choice.lower()=='s'):
                winner_check(comp_choice, user_choice)
            else:
                raise ValueError("Please Enter Correct Value - [R]ock, [P]aper or [S]icsor")
        except ValueError as err:
            print("Oh No ! That's Not a Correct Value")
            print('({})'.format(err))
        choice = input("Do You want to play More(y/n) - ")

if __name__ == '__main__':
    game_start()      