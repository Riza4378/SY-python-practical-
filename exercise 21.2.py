guests = ["Rahul", "Priya", "Amit", "Sneha"]

attendees = 0

print("Event Registration Manager")

for guest in guests:
    print("\nGuest:", guest)
    rsvp = input("Will you attend? (yes/no): ").strip().lower()

    if rsvp == "yes":
        attendees += 1

print("\nFinal Event Summary")
print("Total invited guests:", len(guests))
print("Total expected attendees:", attendees)
print("Total not attending:", len(guests) - attendees)
