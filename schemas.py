from pydantic import BaseModel

class AnswerSchema(BaseModel):
    id: int
    user_id: int
    answer_to: int
    answer_text: str


class QuestionSchema(BaseModel):
    id: int
    question_type: str
    choices: list[str]
    question_text: str | None
    question_image: str | None


class FormSchema(BaseModel):
    id: int
    created_by: int
    name: str
    description: str | None


class UserSchema(BaseModel):
    id: int
    name: str
    email: str
