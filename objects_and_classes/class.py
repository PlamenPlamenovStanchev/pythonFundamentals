# class Class:
#     __students_count = 22
#
#     def __init__(self, name):
#         self.name = name
#         self.students =[]
#         self.grades =[]
#
#     def add_student(self, name, grade):
#         if len(self.students) < self.__students_count:
#             self.students.append(name)
#             self.grades.append(grade)
#
#     def get_average_grade(self):
#         if not self.grades:
#             return 0.00
#         average_grade = sum(self.grades)/len(self.grades)
#         return f"{average_grade:.2f}"
#
#     def __repr__(self):
#         students_str = ", ".join(self.students)
#         average_grade = self.get_average_grade()
#         return f"The students in {self.name}: {students_str}. Average grade: {average_grade}"
#
# class1 = Class("10B")
# class1.add_student ("Pesho", 4.80)
# class1.add_student("Maria", 6.00)
# class1.add_student("Gosho", 5.50)
# print(class1)

class Class:
    __students_count = 22

    def __init__(self, name: str):
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, name: str, grade: float):
        if Class.__students_count > len(self.students):
            self.students.append(name)
            self.grades.append(grade)

    def get_average_grade(self):
        average_grade = sum(self.grades) / len(self.grades)
        return float(f"{average_grade:.2f}")

    def __repr__(self):
        students = ", ".join(self.students)
        average_grade = self.get_average_grade()
        return f"The students in {self.name}: {students}. Average grade: {average_grade}"
