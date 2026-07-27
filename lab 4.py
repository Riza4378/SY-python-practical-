print("----traffic signal simulation system-----")

signal=input(" Enter a signal color :")

if signal=="red":
    print("signal: red")
    print("action: stop")
    
elif signal=="yellow":
    print("signal: yellow ")   
    print("action: get ready") 
    
elif signal=="green":
    print("signal: green")
    print("action: go!!")
    
else:
    print("invalid color!! Please enter Red, Yellow, or Green.")        
