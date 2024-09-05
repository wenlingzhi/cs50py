from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
all_fonts = figlet.getFonts()

def printFont(str,font_name):
    figlet.setFont(font = font_name)
    print(figlet.renderText(str))

if (len(sys.argv) == 1):
    user_input = input("Input: ")
    font_name = random.choice(all_fonts)
    printFont(user_input, font_name)

elif(len(sys.argv) == 3):
    if(sys.argv[1] not in ["--font","-f"]):
        sys.exit("Invalid usage")

    if(sys.argv[2] not in all_fonts):
        sys.exit("Invalid usage")

    user_input = input("Input: ")
    printFont(user_input, sys.argv[2])

else:
    sys.exit("Invalid usage")


