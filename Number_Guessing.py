import random
attempts = []
def score():
    if len(attempts) < 1:
        print("There is no Attempts to Play the game yet")
    else:
        print("The Current High Score is {}".format(min(attempts)))
def start_game():
    choice = input("Hello User, Do you wanna play a Mind Tricking Guess Game(y/n)")
    
    att = 0
    score()
 
    a = 'y'
    while(choice.lower() == 'y'):
        rand_num = int(random.randint(1,11))
        while(a=='y'):
            att+=1
            num = int(input("Enter your Guess (1-10)"))
            if(num == rand_num):
                print("You Guessed it Correct")
                print("You Completed the Game in {} attempts".format(att))
                attempts.append(att)
                break
            elif(num < rand_num):
                print("Its lower")
            elif(num > rand_num):
                print("Its higher")
        choice = input("Do You Want to Play The Game Again(y/n)")
        score()
        att = 0
        
if __name__ == '__main__':
    start_game()

