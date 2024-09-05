import re


def main():
    print(count(input("Text: ")))


def count(s):
    s = s.lower()
    matches = re.findall(r'\bum\b',s)
    return len(matches)




if __name__ == "__main__":
    main()
