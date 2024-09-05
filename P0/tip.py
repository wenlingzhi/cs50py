def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # $14.32
    dollars = float(d[1:])
    return dollars

def percent_to_float(p):
    # 15%
    percent = float(p[:-1])* 0.01
    return percent

main()
