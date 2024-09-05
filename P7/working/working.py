import re
import sys

def main():
    try:
        print(convert(input("Hours: ")))
    except ValueError:
        print("ValueError")
        sys.exit(1)

def convert(s):
    matches = re.search(r"^((?:\d|1[0-2])(?::[0-5][0-9])?) (AM|PM) to ((?:\d|1[0-2])(?::[0-5][0-9])?) (AM|PM)$", s)
    if matches:
        return converts(matches.group(1), matches.group(2)) + " to " + converts(matches.group(3), matches.group(4))
    raise ValueError("Invalid input format")

def converts(time, period):
    if len(time.split(":")) == 1:  # No minutes in time
        if period == "AM":
            if int(time) == 12:
                time = 0
                return f"{time:02}:00"
            return f"{int(time):02}:00"
        else:  # PM case
            if int(time) == 12:
                return f"{int(time):02}:00"
            hour = int(time) + 12
            return f"{hour:02}:00"

    else:  # Time includes minutes
        hour, min = time.split(":")
        hour = int(hour)
        if period == "PM" and hour != 12:
            hour += 12
        elif period == "AM" and hour == 12:
            hour = 0
        return f"{hour:02}:{min}"

if __name__ == "__main__":
    main()
