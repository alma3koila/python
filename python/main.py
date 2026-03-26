name=str(input("Enter student name:"))
Math=float(input("Enter Math grade:"))
Physics=float(input("Enter Physics grade:"))
Python=float(input("Enter Python grade:"))

average=(Math+Physics+Python)/3

if average>=90:
 scholarship=35000
else:
 scholarship=0

gpa=average/25

print("="*35)
print("       STUDENT REPORT CARD      ")
print("="*35)
print("Student :", name)
print("Math :", Math)
print("Physics :", Physics)
print("Python :", Python)
print("-"*32)
print("Average :", round(average, 2))
print("GPA;", round(gpa, 2))
print("Scholarship:", scholarship)
print("="*35)



print("Scholarship granted:", average >= 90)
print("Perfect score:", gpa == 4)
