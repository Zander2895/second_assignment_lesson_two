attendees = int(input("Enter number of attendees: "))
venue = "large hall " if attendees > 100 else "conference room "
print(venue)

facilities = "audio system " if attendees > 100 else "projector "
print(facilities)