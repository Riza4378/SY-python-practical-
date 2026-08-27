status =  input("Enter Atmospheric Status:").lower()

if status == "hot":
    print(" Recommendation : Turn on AC.")

elif status == "cold":
    print("Recommendation : Activate heater.")

elif status == "normal":
    print(" Recommendation : Idle.")

else:
    print("invalid Atmospheric status.")
    