import random

def check(dm):
    for values in dm:
        if values == '_':
            return 1
    
    return 0

def movie_name(movie):
    x = ""
    return(x.join(movie))


letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
movies_list = ['MAIN TERA HERO', 'BAHUBALI']
mov = random.choice(movies_list)


attempts = 10
movies = list(mov)
guess= []
for i in range(len(movies)):
    if(movies[i] == ' '):
        guess.append(' ')
    else:
        guess.append('_')


win = 1
print(guess)
while(attempts > 0 and win == 1):
    
    print(letters)
    print("\n\nAttempts Left - ",attempts)
    user_input = input("Enter Your Guess - ")
    try:
        if user_input.upper() in letters:
            letters.remove(user_input.upper())
            flag = 0
        elif user_input == '':
            raise EOFError
        else:
            raise ValueError
    except ValueError as err:
        print("You have already choosen this value, Choose different Value")
        flag = 1
    except EOFError:
        print("Value is Null")
        flag =1
    
    
    for i in range(len(movies)):
        if(user_input.upper() == movies[i]):
            guess[i] = user_input.upper()
            flag = 1
            if(user_input.upper() in movies):
                continue
            else:
                break
    if(flag == 0):
        attempts-=1
    
    print(guess)
    print("\n")

    win = check(guess)

name  = movie_name(guess)
print(name)
