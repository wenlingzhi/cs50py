def get_info():
    while True:
        try:
            user_in = input("Fraction: ").strip().split('/')
            if (len(user_in) == 2 and int(user_in[0]) <= int(user_in[1])):
                return round(int(user_in[0]) / int(user_in[1]),2)
        except ValueError:
            pass
        except ZeroDivisionError:
            pass

fraction = int(get_info()*100)
if fraction >= 99:
    print("F")
elif fraction <= 1:
    print("E")
else:
    print(f"{fraction}%")

