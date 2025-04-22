from typing import List, TypeVar, Generic
from abc import ABC, abstractmethod
import random

### Base Classes ###

class Assessment(ABC):
    def __init__(self, title: str):
        self.title = title

    @abstractmethod
    def grade(self, submission: str) -> str:
        pass

class Quiz(Assessment):
    def grade(self, submission: str) -> str:
        grade = random.choice(['A', 'B', 'C', 'D', 'F'])
        print(f"Grading quiz '{self.title}' automatically. Grade: {grade}")
        return grade

class Assignment(Assessment):
    def grade(self, submission: str) -> str:
        grade = random.choice(['A', 'B', 'C', 'D', 'F'])
        print(f"Grading assignment '{self.title}' manually. Grade: {grade}")
        return grade

T = TypeVar('T', bound=Assessment)

class Course(Generic[T]):
    def __init__(self, name: str, instructor: str):
        self.name = name
        self.instructor = instructor
        self.assessments: List[T] = []

    def add_assessment(self, assessment: T):
        self.assessments.append(assessment)
        print(f"Assessment '{assessment.title}' added to course '{self.name}'.")

    def grade_all(self):
        print(f"\nGrading all assessments in course '{self.name}':")
        for assessment in self.assessments:
            assessment.grade("sample submission")


### User System ###

class User(ABC):
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    @abstractmethod
    def get_role(self) -> str:
        pass

class Student(User):
    def get_role(self) -> str:
        return "Student"

    def submit_assignment(self, assessment: Assessment, submission: str):
        print(f"{self.name} submitted '{assessment.title}' with content: {submission}")

class Instructor(User):
    def get_role(self) -> str:
        return "Instructor"

    def assign_assessment(self, course: Course, assessment: Assessment):
        course.add_assessment(assessment)

    def grade_student(self, assessment: Assessment, submission: str) -> str:
        print(f"{self.name} is grading '{assessment.title}'")
        return assessment.grade(submission)

class Admin(User):
    def get_role(self) -> str:
        return "Admin"

    def create_course(self, name: str, instructor: str) -> Course:
        print(f"Course '{name}' has been created with instructor '{instructor}'.")
        return Course(name, instructor)

    def remove_course(self, course: Course, courses: List[Course]):
        if course in courses:
            courses.remove(course)
            print(f"Course '{course.name}' has been removed.")
        else:
            print(f"Course '{course.name}' not found.")

    def create_user(self, name: str, email: str, role: str, users: List[User]):
        role_lower = role.lower()
        if role_lower == "instructor":
            user = Instructor(name, email)
        elif role_lower == "student":
            user = Student(name, email)
        elif role_lower == "admin":
            user = Admin(name, email)
        else:
            print(f"Invalid role: {role}")
            return
        users.append(user)
        print(f"User '{name}' with role '{role}' has been created. ")

    def delete_user(self, user: User, users: List[User]):
        if user in users:
            users.remove(user)
            print(f"User '{user.name}' has been deleted.")
        else:
            print(f"User '{user.name}' not found.")


### Main Function for Testing ###

def main():
    # Admin setup
    admin = Admin("Alice", "alice@example.com")
    users: List[User] = []
    courses: List[Course] = []

    # Create users
    admin.create_user("Bob", "bob@example.com", "Instructor", users)
    admin.create_user("Charlie", "charlie@example.com", "Student", users)
    print("\n")

    # Extract created users
    instructor = next((u for u in users if isinstance(u, Instructor)), None)
    student = next((u for u in users if isinstance(u, Student)), None)

    # Create course
    course = admin.create_course("Intro to Python", instructor.name if instructor else "Unknown")
    print("\n")
    courses.append(course)

    # Instructor adds assessments
    quiz = Quiz("Week 1 Quiz")
    assignment = Assignment("Project 1")
    if instructor:
        instructor.assign_assessment(course, quiz)
        instructor.assign_assessment(course, assignment)

    # Student submits and instructor grades
    if student and instructor:
        student.submit_assignment(quiz, "My answers for quiz")
        instructor.grade_student(quiz, "My answers for quiz")

        student.submit_assignment(assignment, "My code project")
        instructor.grade_student(assignment, "My code project")

    # Grade all assessments in course
    course.grade_all()

    # Display all users
    print("\nCurrent users:")
    for user in users:
        print(f"- {user.name} ({user.get_role()})")

    # Remove course
    admin.remove_course(course, courses)

if __name__ == "__main__":
    main()
