user = input("Expression: ").split()
num1 = float(user[0])
signal = user[1]
num2 = float(user[2])
match signal:
    case "+":
        print(f"{(num1 + num2):.1f}")
    case "-":
        print(f"{(num1 - num2):.1f}")
    case "*":
        print(f"{(num1 * num2):.1f}")
    case "/":
        print(f"{(num1 / num2):.1f}")
