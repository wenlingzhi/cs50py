import re
month_mapping = {
    "January":1,
    "February":2,
    "March":3,
    "April":4,
    "May":5,
    "June":6,
    "July":7,
    "August":8,
    "September":9,
    "October":10,
    "November":11,
    "December":12
}
# 9/8/1636 or September 8, 1636 out:1636-03-05
def main():
    while True:
        try:
            date = input("Date: ").title().strip()
            list1 = date.split("/")
            pattern = r'(\w+) (\d+), (\d+)'
            matches = re.findall(pattern, date)

            if matches:
                match = matches[0]
                month = match[0]
                day = match[1]
                year = match[2]

                if not check_month(month_mapping[month]):
                    continue
                if not check_day(day):
                    continue

                if month in month_mapping and day.isdigit() and year.isdigit():
                    mon = int(month_mapping[month])
                    day = int(match[1])
                    print(f"{year}-{mon:02}-{day:02}")
                    break

            elif (''.join(list1).isdigit() and len(list1) == 3):
                year = int(list1[2])
                mon = int(list1[0])
                day = int(list1[1])

                if not check_month(mon):
                    continue
                if not check_day(day):
                    continue
                print(f"{year}-{mon:02}-{day:02}")
                break

        except ValueError:
            pass
        except IndexError:
            pass

def check_month(mon):
    if (1<=int(mon)<=12):
        return True
    else:
        return False

def check_day(day):
    if (1<=int(day)<=31):
        return True
    else:
        return False

main()
'''
import re
from datetime import datetime

MONTH_MAPPING = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

def parse_date(date_str):
    # Match "Month Day, Year" format
    match = re.match(r'(\w+) (\d+), (\d+)', date_str)
    if match:
        month_name, day, year = match.groups()
        month = MONTH_MAPPING.get(month_name)
        if month and day.isdigit() and year.isdigit():
            return year, month, int(day)

    # Match "MM/DD/YYYY" format
    try:
        month, day, year = map(int, date_str.split('/'))
        if 1 <= month <= 12 and 1 <= day <= 31:
            return year, month, day
    except (ValueError, IndexError):
        pass

    return None

def main():
    while True:
        date_str = input("Date: ").title().strip()
        parsed_date = parse_date(date_str)
        if parsed_date:
            year, month, day = parsed_date
            try:
                # Validate the date
                datetime(year, month, day)
                print(f"{year}-{month:02}-{day:02}")
                break
            except ValueError:
                print("Invalid date. Please try again.")
        else:
            print("Invalid format. Please try again.")

if __name__ == "__main__":
    main()

'''
