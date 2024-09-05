# (A, E, I, O, and U) omitted
def main():
    user_input = input("Input: ")
    print(shorten(user_input))

def shorten(str):
    vowels_to_omit = ['a', 'e', 'i', 'o', 'u']
    output = ""

    for char in str:
        if char.lower() not in vowels_to_omit:
            output += char
    return output

if __name__ == "__main__":
    main()




'''
omit = ['a','e','i','o','u']
output = []
user_input = input("Input: ")
for i in user_input:
    if(i.lower() in omit):
        continue
    else:
        output += i
result = "".join(output)
print(result)
'''
