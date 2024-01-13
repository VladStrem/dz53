class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Person: {self.name}, Age: {self.age}")


class Student(Person):
    def __init__(self, name, age, person_id):
        super().__init__(name, age)
        self.person_id = person_id

    def introduce(self):
        print(f"Student: {self.name}-{self.person_id}, Age: {self.age}")

    def study(self, subject):
        print(f"Student {self.name}-{self.person_id} is studying {subject}.")


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def introduce(self):
        print(f"Teacher: {self.name}, Age: {self.age}, Subject: {self.subject}")

    def teach(self, student):
        if isinstance(student, Student):
            print(f"Teacher {self.name} teaches {self.subject} to student {student.name}-{student.person_id}.")
        else:
            print("Invalid student object provided.")


class Employee(Person):
    def __init__(self, name, age, salary, specialty):
        super().__init__(name, age)
        self.salary = salary
        self.specialty = specialty

    def introduce(self):
        print(f"Employee: {self.name}, Age: {self.age}, Specialty: {self.specialty}, Salary: {self.salary}")

    def work(self):
        print(f"Employee {self.name} is working as a {self.specialty} and earns a salary of {self.salary}.")


print(f"Person mro: {Person.__mro__}")
print(f"Student mro: {Student.__mro__}")
print(f"Teacher mro: {Teacher.__mro__}")
print(f"Employee mro: {Employee.__mro__}")



















