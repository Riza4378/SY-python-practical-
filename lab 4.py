print("************ traffic signal simulation system ************")

signal = input("enter a signal color: ").lower()

if signal == "red":
    print("signal is red")
    print("action: stop")

elif signal == "yellow":
    print("signal is yellow")
    print("action: get ready")

elif signal == "green":
    print("signal is green")
    print("action: go")

else:
    print("invalid color! enter red, yellow, or green.")