#challenge 3.2
class Student:

    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = float(cgpa)  # Convert cgpa to float

    @staticmethod  # Decorator to make it a static method
    def sort_students(student_list):
        sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
        return sorted_students

students = [  # Fixed the variable name here from "student" to "students"
    Student("pooja", "A123", "9.9"),
    Student("anitha", "A124", "9.8"),
    Student("hari", "A1215", "9.7"),
    Student("varshini", "A126", "9.6")
]
sorted_students = Student.sort_students(students)  # Corrected the function call

for student in sorted_students:
    print("name: {}, rollnumber: {}, cgpa: {}.".format(student.name, student.roll_number, student.cgpa))
  