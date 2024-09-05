def store_dict():
    list_dict = {}
    while True:
        try:
            key = input().strip().upper()
            if key in list_dict:
                list_dict[key] += 1
            else:
                list_dict[key] = 1
        except ValueError:
            pass
        except EOFError:
            print("")
            return list_dict

def show_list(dict):
    for item in sorted(dict):
        print(dict[item],item)

show_list(store_dict())
