user = input("Greeting: ").lower().strip()

if(user.startswith("hello")):
    print("$0",end = "")
elif(user.startswith("h")):
    print("$20",end = "")
else:
    print("$100",end = "")
