def main():
    time = input("What time is it? ")
    utime = convert(time)

    #eat breakfast between 7:00 and 8:00, lunch between 12:00 and 13:00, and dinner between 18:00 and 19:00.
    if( 7<= utime <=8):
        print("breakfast time")
    elif(12 <= utime <= 13):
        print("lunch time")
    elif(18 <= utime <= 19):
        print("dinner time")

def convert(time):
    time_list = time.split(":")
    num1 = float(time_list[0])
    num2 = float(time_list[1])/60
    return num1+num2


if __name__ == "__main__":
    main()
