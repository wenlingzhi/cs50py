import random

def main():
    count = 0
    right = 0
    level = get_level()

    while count < 10:
        x,y = generate_integer(level)
        miss = 0
        count += 1

        while True:
            try:
                user_input = int(input(f"{x} + {y} = "))

            except ValueError:
                print("EEE")
                miss += 1
                if miss == 3:
                    print(f"{x} + {y} = {x + y}")
                    break

            else:
                if user_input == (x+y):
                    right += 1
                    break
                else:
                    print("EEE")
                    miss += 1
                    if(miss == 3):
                        print(f"{x} + {y} = {x+y}")
                        break

    print(f"Score: {right}")

def get_level():
    while True:
        try:
            user_input = int(input("Level: "))
            if user_input in [1,2,3]:
                return user_input
            else:
                pass
        except ValueError:
            pass

def generate_integer(level):
    while True:
        if level == 1:
            return [random.randint(0,9),random.randint(0,9)]
        elif level == 2:
            return [random.randint(10,99),random.randint(10,99)]
        elif level == 3:
            return [random.randint(100,999),random.randint(100,999)]

if __name__ == "__main__":
    main()
