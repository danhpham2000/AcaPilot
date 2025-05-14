from pydantic import BaseModel
from typing import List


class QAQuiz(BaseModel):
    """
    A question with question and typing answers, along with explanation, or correct to check the similarity
    """

    question: str
    user_answer: str
    correct_answer: str
    type: str = "Opened answer"


class ChoiceAnswer(BaseModel):
    """
    A answer with choice and explanation
    """
    choice: str
    explanation: str


class MultipleChoiceQuiz(BaseModel):
    """
    A list multiple choice answers that contain choices and correct answers
    """
    question: str
    choice: List[ChoiceAnswer]
    correct_answer: ChoiceAnswer
    type: str = "Multiple choice"


class ListOfMCQuizzes(BaseModel):
    questions: List[MultipleChoiceQuiz]

class ListOfQAQuizzes(BaseModel):
    questions: List[QAQuiz]



class AssignmentInfo(BaseModel):
    """
    This provides information about the future quiz or exam
    """
    name: str
    description: str
    assignment_date: str


class ClassInfo(BaseModel):
    """
    The important information such as exam exam date, quizzes, homework from the document
    """
    class_name: str
    assignments: List[AssignmentInfo]
    class_duration: int



class Resource(BaseModel):
    title: str
    description: str

class Roadmap(BaseModel):
    resources: List[Resource]