# Course Lookup Pseudocode
# Start
#
# Create a dictionary named room_numbers:
#   CSC101: 3004
#   CSC102: 4501
#   CSC103: 6755
#   NET110: 1244
#   COM241: 1411
#
# Create a dictionary named instructors:
#   CSC101: Haynes
#   CSC102: Alvarado
#   CSC103: Rich
#   NET110: Burke
#   COM241: Lee
#
# Create a dictionary named meeting_times:
#   CSC101: 8:00 a.m.
#   CSC102: 9:00 a.m.
#   CSC103: 10:00 a.m.
#   NET110: 11:00 a.m.
#   COM241: 1:00 p.m.
#
# Prompt the user to enter a course number
# Read course_number
#
# If course_number exists in room_numbers:
#   Display the room number, instructor, and meeting time for that course
#
# End



# Create a dictionary for course and room number
room_numbers = {
    "CSC101": "3004",
    "CSC102": "4501",
    "CSC103": "6755",
    "NET110": "1244",
    "COM241": "1411"
}

# Create a dictionary for course and instructor
instructors = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee"
}

# Create a dictionary for course and meeting time
meeting_times = {
    "CSC101": "8:00 a.m.",
    "CSC102": "9:00 a.m.",
    "CSC103": "10:00 a.m.",
    "NET110": "11:00 a.m.",
    "COM241": "1:00 p.m."
}

# Get the course number
course_number = input("Enter a course number: ")


# Use an if statement to decide which course information to display
if course_number in room_numbers:
    # Look up values from each dictionary
    room = room_numbers[course_number]
    instructor = instructors[course_number]
    time = meeting_times[course_number]

    # Print the results (comma-separated)
    print("Course Number:", course_number)
    print("Room Number:", room)
    print("Instructor:", instructor)
    print("Meeting Time:", time)
