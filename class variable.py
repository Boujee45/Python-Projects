class Student:
    '''Class variable'''
    class_year = 2024
    new_students = 0

    def __init__(self,name,age):
        self.name = name
        self.age = age
        Student.new_students += 1

student1 = Student("Him",23)
'''print(student1.name)
print(student1.age)'''
student2 = Student("Jane", 21)
student3 = Student("Oscar", 20)
student4 = Student("June", 30)

print(f"Graduating class of {Student.class_year} has {Student.new_students} students")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)


