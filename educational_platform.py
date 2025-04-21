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
    def __init__(self, name: str):
        self.name = name
        self.assessments: List[T] = []

    def add_assessment(self, assessment: T):
        self.assessments.append(assessment)

    def grade_all(self):
        for assessment in self.assessments:
            assessment.grade()

#Complete your main function here
