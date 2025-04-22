from typing import List, TypeVar, Generic
from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, user_id: int, name: str, email: str):
        self.user_id = user_id
        self.name = name
        self.email = email

    @abstractmethod
    def role(self) -> str:
        ...

class Student(User):
    def get_role(self)->str:
        return "Student"

#user may need to change depending on what its called
class Instructor(User):
   def get_role(self) -> str:
        return "Instructor"

    def assign_assessment(self, course: Course, assessment: Assessment):
        course.add_assessment(assessment)

    def grade_student(self, assessment: Assessment, submission: str) -> float:
        print(f"{self.name} grading {assessment.title}")
        return assessment.grade(submission)

class Assessment(ABC):
    def grade(self, submission: str) -> float:
        rand_num = random.randint(1, 5)
        print(f"Grading assignment: {self.title} manually.")
        if rand_num == 1:
            x = "F"
        elif rand_num == 2:
            x = "D"
        elif rand_num == 3:
            x = "C"
        elif rand_num == 4:
            x = "B"
        else:
            x = "A"
        print(f"Grade: {x}")
        return x

class Quiz(Assessment):
   def grade(self, submission: str) -> float:
        rand_num = random.randint(1, 5)
        print(f"Grading quiz: {self.title} automatically.")
        if rand_num == 1:
            x = "F"
        elif rand_num == 2:
            x = "D"
        elif rand_num == 3:
            x = "C"
        elif rand_num == 4:
            x = "B"
        else:
            x = "A"
        print(f"Grade: {x}")
        return x

class Assignment(Assessment):
    def grade(self):
        print(f"Grading assignment: {self.title} manually.")

T = TypeVar('T', bound=Assessment)

class Course(Generic[T]):
    def __init__(self, name: str):
        self.name = name
        self.assessments: List[T] = []

    def add_assessment(self, assessment: T):
        self.assessments.append(assessment)

    def grade_all(self):
        for assessment in self.assessments:
            assessment.grade()

def main():
    instructor = Instructor("Dr. Smith", "smith@university.edu")
    student = Student("Jane Doe", "jane@student.edu")

    course = Course(name="Intro to CS")

    quiz1 = Quiz("Week 1 Quiz")
    assignment1 = Assignment("Project 1")

    instructor.assign_assessment(course, quiz1)
    instructor.assign_assessment(course, assignment1)

    instructor.grade_student(quiz1, "quiz answers")
    instructor.grade_student(assignment1, "assignment content")

if __name__ == "__main__":
    main()
