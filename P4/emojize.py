'''
>>> print(emoji.emojize('Python is :thumbs_up:'))
Python is 👍
'''
from emoji import emojize
user_input = input("Input: ")
if "_" not in user_input and "thumbsup" not in user_input:
    print(emojize(user_input))
else:
    print(emojize(user_input,language='alias'))
