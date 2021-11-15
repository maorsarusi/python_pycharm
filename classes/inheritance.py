import random

NAMES = ["Meir", "Avraham", "David", "Yossi"]


class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __str__(self):
        return "the Person {} is {} years old".format(self.__name, self.__age)

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


class Student(Person):
    def __init__(self, name="", age=0, num_of_exams=0, grades_avg=0):
        super(Student, self).__init__(name, age)
        self.__num_of_exams = num_of_exams
        self.__grades_avg = grades_avg

    def set_avg(self, grade):
        grades = grade + self.get_avg() * self.__num_of_exams
        self.another_exam()
        avg = grades / self.__num_of_exams
        self.__grades_avg = avg

    def get_avg(self):
        return self.__grades_avg

    def another_exam(self):
        self.__num_of_exams += 1

    def __str__(self):
        return "The Student {} is {} years old, done {} exams and it's average grades are: {}".format(self.get_name(),
                                                                                                      self.get_age(),
                                                                                                      self.__num_of_exams,
                                                                                                      self.get_avg())


def main():
    students_list = []
    for name in NAMES:
        age = random.randint(20, 25)
        num_of_exams = random.randint(1, 10)
        avg = random.randint(56, 100)
        student = Student(name, age, num_of_exams, avg)
        students_list += [student]

    print("before exam:")
    for student in students_list:
        print(student)
        grade = random.randint(0, 100)
        print("the student grade is: {}".format(grade))
        student.set_avg(grade)
    print("after exam:")
    for student in students_list:
        print(student)



if __name__ == "__main__":
    main()
