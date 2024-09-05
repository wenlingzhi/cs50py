def main():
    user_name = []
    get_name(user_name)
    if len(user_name) == 1:
        print(f"Adieu, adieu, to {user_name[0]}")
    elif len(user_name) == 2:
        print(f"Adieu, adieu, to {user_name[0]} and {user_name[1]}")
    else:
        name_str = ", ".join(user_name[:-1])
        print(f"Adieu, adieu, to {name_str}, and {user_name[-1]}")

def get_name(list):
  while True:
    try:
        list.append(input("Name: "))
    except EOFError:
        pass
        break

main()
