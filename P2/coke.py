def get_coin():
    while True:
        coin = int(input("Insert Coin: "))
        if (coin == 25 or coin == 10 or coin == 5):
            return coin
        else:
            return 0

def main():
    amount = 50
    while (amount >= 0):
        print("Amount Due:",amount)
        coin = get_coin()
        amount -= coin
        if(amount <= 0):
            print("Change Owed:",-amount)
            break

main()

