class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"{self.name} is {self.age} years old")

class Grade(Student):
    def __init__(self, name, age,grade):
        super().__init__(name, age)
        self.grade= grade
    
    def gradeDisp(self):
        print(self.grade)

student1 = Student("Abebe", 16)
print(student1.name)
student1.display()

student2 = Student("Alemu", 20)
print(student2.name)
student2.display()

student1 = Grade("Abebe",16, 3.95)
student1.gradeDisp()