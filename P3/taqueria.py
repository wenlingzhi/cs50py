menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def get_item():
    total = 0
    while True:
        try:
            item = input("Item: ").title()
            if item in menu:
                total += float(menu[item])
                print(f"${total:.2f}")
        except ValueError:
            pass
        except EOFError:
            print("")
            break

get_item()
