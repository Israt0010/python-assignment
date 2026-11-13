# Student Grade Calculator

# Taking student's name
name = input("Enter Student Name: ")

print()
# Taking marks for 3 subjects
subject1 = float(input("Enter marks for Subject 1:"))
subject2 = float(input("Enter marks for Subject 2:"))
subject3 = float(input("Enter marks for Subject 3:"))

print()

# Calculating total marks
total = subject1 + subject2 + subject3

print()

# Calculating average marks
average = total/3

print()
# Determining grade
if average >= 80:
    grade = "A+"
elif average >= 70:
    grade = "A"
elif average >= 60:
    grade = "B"
elif average >= 50:
    grade = "C"
else:
    grade = "F"

print()
# Displaying result using f-string

print(f"Student Name: {name}")
print(f"Total Marks: {total}")
print(f"Average: {average:.2f}")
print(f"Grade: {grade}")
