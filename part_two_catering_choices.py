attendees = int(input("Enter number of attendees: "))
venue = "large hall " if attendees > 100 else "conference room "
print(venue)

facilities = "audio system " if attendees > 100 else "projector "
print(facilities)

response = input("Would you like vegetarian?: ")
cater = "Veggie Delight Caterers " if response == "Yes" else "Gourmet Meals Caterers "
print(cater)
