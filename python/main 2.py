name=str(input("Enter student name:"))
Math=float(input("Enter Math grade:"))
Physics=float(input("Enter Physics grade:"))
Python=float(input("Enter Python grade:"))


grades = [Math, Physics, Python]
subjects = ["Math", "Physics", "Python"]

average=(Math+Physics+Python)/3

if average >= 90:
    letter_grade = "A"
elif average >= 75:
    letter_grade = "B"
elif average >= 60:
    letter_grade = "C"
elif average >= 50:
    letter_grade = "D"
else:
    letter_grade = "F"

scholarship = average >= 90 and Math >= 70 and Physics >= 70 and Python >= 70

print("=" * 30)
print("Student :", name.upper())
print("Math :", Math)
print("Physics :", Physics)
print("Python :", Python)
print("-" * 30)
print("Average :", average)
print("Letter grade :", letter_grade)
print("Scholarship :", scholarship)
print("=" * 30)

if Math >= 90:
    print("Math :", Math, "-> Excellent")
elif Math >= 75:
    print("Math :", Math, "-> Good")
elif Math >= 60:
    print("Math :", Math, "-> Satisfactory")
else:
    print("Math :", Math, "-> Fail")

if Physics >= 90:
    print("Physics :", Physics, "-> Excellent")
elif Physics >= 75:
    print("Physics :", Physics, "-> Good")
elif Physics >= 60:
    print("Physics :", Physics, "-> Satisfactory")
else:
    print("Physics :", Physics, "-> Fail")

if Python >= 90:
    print("Python :", Python, "-> Excellent")
elif Python >= 75:
    print("Python :", Python, "-> Good")
elif Python >= 60:
    print("Python :", Python, "-> Satisfactory")
else:
    print("Python :", Python, "-> Fail")


print("Name uppercase :", name.upper())
print("Name lowercase :", name.lower())
print("Name length :", len(name))
print("Masked name :", name.replace(name[0], "*", 1))




