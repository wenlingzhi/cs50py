from sys import argv,exit
from PIL import Image,ImageOps

def main():
    is_exit()
    try:
        base_img = Image.open(argv[1])
        shirt = Image.open('shirt.png')
    except FileNotFoundError:
        exit("Input does not exist")

    size = shirt.size
    base_img = ImageOps.fit(base_img,size)
    base_img.paste(shirt,shirt)
    base_img.save(argv[2])

def is_exit():
    if len(argv) < 3:
        exit("Too few command-line arguments")
    elif len(argv) > 3:
        exit("Too much command-line arguments")
    else:
        file1 = argv[1]
        file2 = argv[2]
        if not (is_right_file(file1) and is_right_file(file2)):
            exit("Invalid Input")
        else:
            if not is_same_suffix(file1,file2):
                exit("Input and output have different extensions")

def is_right_file(filename):
    if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
        return True
    else:
        return False

def is_same_suffix(filename1,filename2):
    sf1 = filename1[filename1.rfind(".")+1:]
    sf2 = filename2[filename2.rfind(".")+1:]
    return sf1 == sf2

main()
