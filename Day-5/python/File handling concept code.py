# File Handling

# Write
with open("Day-1.txt", "w") as file:
    file.write("Name: Gokul\n")
    file.write("Age: 22\n")
    file.write("Course: Python\n")


# Read
with open("student.txt", "r") as file:
    data = file.read()
    print(data)


# Append
with open("student.txt", "a") as file:
    file.write("Location: Chithode\n")


# Read updated file
with open("student.txt", "r") as file:
    print(file.read())
        
