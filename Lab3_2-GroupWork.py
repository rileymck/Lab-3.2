from typing import List, TypeVar, Generic
from abc import ABC, abstractmethod

class Assessment(ABC):
    def __init__(self, title: str):
        self.title = title

    @abstractmethod
    def grade(self):
        pass

class Quiz(Assessment):
    def grade(self):
        print(f"Grading quiz: {self.title} automatically.")

class Assignment(Assessment):
    def grade(self):
        print(f"Grading assignment: {self.title} manually.")

T = TypeVar('T', bound=Assessment)

class Course(Generic[T]):
    def __init__(self, name: str, instructor: str):
        self.name = name
        self.instructor = instructor
        self.assessments: List[T] = []

    def add_assessment(self, assessment: T):
        self.assessments.append(assessment)

    def grade_all(self):
        for assessment in self.assessments:
            assessment.grade()

#Complete your main function here

class User(ABC):
    def __init__(self, name:str, email:str):
        self.name = name
        self.email = email

class Student(User): # Child class (inheritance)
    def get_role(self)->str:
        return "Student"
    
    def check_grades(self, assessment: Assessment):
        """Checks the grades of a specific assessment."""
        print(f"Checking grades for {assessment.title}.")
    
    def submit_assignment(self, assignment: Assignment):
        """Submits an assignment."""
        print(f"Submitting assignment: {assignment.title}.")


    def take_quiz(self, quiz: Quiz):
        """Takes a quiz."""
        print(f"Taking quiz: {quiz.title}.")

class Instructor(User):
    """ Instructor class for User """
    def get_role(self):
        return "The role of this user is Instructor"

class Admin(User):
    """ Derived Class of User for Admin Users. """
    def get_role(self):
        return "The role of this user is Admin "
    
    def create_course(self, name: str, instructor: str) -> Course:
        """Creates a new course."""
        print(f"Course '{name}' has been created with instructor '{instructor}'.")
        return Course(name, instructor)
    
    def remove_course(self, course: Course, courses: List[Course]):
        """Removes a course from the system."""
        if course in courses:
            courses.remove(course)
            print(f"Course '{course.name}' has been removed.")
        else:
            print(f"Course '{course.name}' not found.")

    def create_user(self, name: str, email: str, role: str, users: List[User]):
        """Creates a new user and adds them to the system."""
        if role.lower() == "instructor":
            user = Instructor(name, email)
        elif role.lower() == "student":
            user = Student(name, email)
        elif role.lower() == "admin":
            user = Admin(name, email)
        else:
            print(f"Invalid role: {role}")
            return
        users.append(user)
        print(f"User '{name}' with role '{role}' has been created.")

    def delete_user(self, user: User, users: List[User]):
        """Deletes a user from the system."""
        if user in users:
            users.remove(user)
            print(f"User '{user.name}' has been deleted.")
        else:
            print(f"User '{user.name}' not found.")


### Main Function for Testing ###

def main():
    # Create an admin
    admin = Admin("Alice", "alice@example.com")

    # List to store users
    users = []

    # Admin creates users
    admin.create_user("Bob", "bob@example.com", "Instructor", users)
    admin.create_user("Charlie", "charlie@example.com", "Student", users)
    admin.create_user("Dave", "dave@example.com", "Admin", users)

    # Display all users
    print("\nUsers in the system:")
    for user in users:
        print(f"- {user.name} ({user.get_role()})")

    # Admin deletes a user
    admin.delete_user(users[1], users)  # Deletes Charlie

    # Display all users after deletion
    print("\nUsers in the system after deletion:")
    for user in users:
        print(f"- {user.name} ({user.get_role()})")

    # List to store courses
    courses = []

    # Admin creates a course
    course1 = admin.create_course("Math 101", "Bob")
    courses.append(course1)

    # Admin creates another course
    course2 = admin.create_course("Physics 101", "Bob")
    courses.append(course2)

    # Display all courses
    print("\nCourses in the system:")
    for course in courses:
        print(f"- {course.name}")

    # Admin removes a course
    admin.remove_course(course1, courses)

    # Display all courses after removal
    print("\nCourses in the system after removal:")
    for course in courses:
        print(f"- {course.name}")

if __name__ == "__main__":
    main()
