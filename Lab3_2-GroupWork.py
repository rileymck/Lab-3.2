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

class Student(User):
    """ Student class inherited from User """

    def get_role(self): 
        return "Student"

class Instructor(User):
    """ Instructor class for User """
    def role(self):
        return "The role of this user is Instructor"

class Admin(User):
    """ Derived Class of User for Admin Users. """
    def get_role(self):
        return "The role of this user is Admin "
    
    def create_course(self, name:str) -> Course:
        """ Creates a new course. """
        print(f"Course '{name}' has been created.")
        return Course(name)
    
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
