import sys

def main():
    if len(sys.argv) > 2:
        exit("Too many command-line arguments")
    elif len(sys.argv) == 1:
        exit("Too few command-line arguments")
    elif not sys.argv[1].endswith(".py"):
        exit("Not a Python File")
    else:
        try:
            count = 0
            with open(sys.argv[1]) as file:
                for line in file:
                    if not is_space(line):
                        count+=1

        except FileNotFoundError:
            exit("File does not exist")

        print(count,end="")

def is_space(str):
    cond1 = str.strip().startswith("#")
    cond2 = str.isspace()
    return cond1 or cond2

main()
