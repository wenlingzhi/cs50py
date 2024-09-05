import requests
import json
import sys

# ["bpi"] ["USD"] ["rate_float"]

def exchange(num):
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        o = response.json()
        rate = o["bpi"]["USD"]["rate_float"]
        result = rate * num
        print(f"${result:,}")
    except requests.RequestException:
        print("RequestException")
        pass

def main():
    if len(sys.argv)<2:
        sys.exit("Missing command-line argument")
    elif len(sys.argv)>2:
        sys.exit("too much command-line arguments")
    else:
        try:
            num = float(sys.argv[1])
        except ValueError:
            sys.exit("Command-line argument is not a number")
        exchange(num)
main()
