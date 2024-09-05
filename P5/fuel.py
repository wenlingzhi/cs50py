def main():
    while True:
        try:
            percentage = convert(input("Fraction: "))
            print(gauge(percentage))
            break
        except ValueError:
            pass
        except ZeroDivisionError:
            pass

def convert(fraction):
        x,y = fraction.split("/")
        x,y = int(x),int(y)
        if y == 0:
            raise ZeroDivisionError
        elif y < x:
            raise ValueError
        return int(round((x/y)*100))

def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
