from pydantic import BaseModel


class GetQuestionsRequest(BaseModel):
    technology: str


class GetQuestionSetRequest(BaseModel):
    technology: str