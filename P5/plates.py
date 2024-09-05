'''
“All vanity plates must start with at least two letters.”

“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”

“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”

“No periods, spaces, or punctuation marks are allowed.”

'''
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    alpha_list = ""
    num_list = ""

    if(len(s)<2 or len(s)>6):
        return False

    if(not (s[0].isalpha() and s[1].isalpha())):
        return False

    if(s.isalpha()):
        return True

    for i in range(len(s)-1):
        if (s[i].isalpha() and s[i+1].isdigit):
            alpha_list = s[:i+1]
            num_list = s[i+1:]

    return(alpha_list.isalpha() and num_list.isdigit() and num_list[0]!="0")

if __name__ == "__main__":
    main()
