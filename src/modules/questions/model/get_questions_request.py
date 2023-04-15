from pydantic import BaseModel


class GetQuestionsRequest(BaseModel):
    technology: str


class SetQuestionRequest(BaseModel):
    title: str
    technology: str
    answer: int
    answers: list[str]


class GetQuestionSetRequest(BaseModel):
    technology: str