coordinates = (17.279, 74.546)

print("GPS Coordinates:", coordinates)

print("First Coordinate:", coordinates[0])
print("Second Coordinate:", coordinates[1])

latitude = coordinates[0]
longitude = coordinates[1]

print("Latitude:", latitude)
print("Longitude:", longitude)
print("Total Coordinates:", len(coordinates))

if 17.279 in coordinates:
    print("Latitude is available in the tuple.")

if 74.546 in coordinates:
    print("Longitude is available in the tuple.")


print("Sliced Coordinates:", coordinates[0:1])


new_coordinates = coordinates + (18.520, 73.856)
print("Concatenated Coordinates:", new_coordinates)