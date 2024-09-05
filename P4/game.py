import random
def get_num(str):
    while True:
        try:
            user_input = int(input(str))
        except ValueError:
            pass
        else:
            return user_input

def guess_game():
    while True:
        try:
            num = random.randint(1,get_num("Level: "))
            break
        except ValueError:
            pass

    while True:
        answer = get_num("Guess: ")
        if answer > num:
            print("Too large!")
        elif answer < num:
            print("Too small!")
        else:
            print("Just right!")
            break

guess_game()
