from datetime import date
import re
import inflect
p = inflect.engine()

def main():
    try:
        birthday = get_time(input("Date of Birth: "))
        today = date.today()
        minitus = ((today-birthday).days)*1440
        result = p.number_to_words(minitus, andword="").capitalize()
        print(f"{result} minutes")
    except ValueError as e:
        exit(e)

def get_time(s):
    match = re.search(r"^(\d{4})-(\d\d)-(\d\d)$",s)
    if not match:
        exit("Invalid date")
    year,mon,day = match.groups()
    return date(int(year),int(mon),int(day))

if __name__ == "__main__":
    main()
