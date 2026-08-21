feedback=input("Enter Your Feedback:")
print("feedback format report".upper().center(85))

print("\n original feedback:".title())
print("\n")
print("Feedback Summary".title())
print("total word count:".title(),len(feedback.split()))
print("total character count:".title(),len(feedback))
print("total Spaces count:".title(),feedback.count(" "))
print("total exclamation:".title(),feedback.count("!"))

print("\n===================================================\n")

print("formatted feedback:".lstrip())
print("\n")

print("Uppercase Feedback:",feedback.upper())
print("Lowercase Feedback:",feedback.lower())
print("Title Feedback:",feedback.title())
print("Capitalize Feedback:",feedback.capitalize())
print("Swapcase Feedback:",feedback.swapcase())

print("\n======================================================\n")

print("professional feedback:".capitalize())
print("\n")
print("Words split=",feedback.split())

print("thank you for your valuable feedback".center(85).upper())