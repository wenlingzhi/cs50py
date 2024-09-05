def convert(text):
    text = text.replace(":)","🙂").replace(":(","🙁")
    print(text)

def main():
    string = input()
    convert(string)
    
if __name__ == "__main__":
    main()
