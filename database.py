from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy import select, update, insert,  ScalarResult

from models import *
from config import settings
from schemas import *

engine = create_async_engine(
    url=settings.DB_URL,
    echo=False,
    pool_size=5,
    max_overflow=10
)


async def get_form(id: int) -> Form | None:
    async with AsyncSession(autoflush=False, bind=engine) as db:
        q = select(Form).where(Form.id == id)
        res = await db.execute(q)
        return res.first()


async def answer_form(answers: list[AnswerSchema]) -> None:
    parsed_answers: list[Answer] = []
    for answer in answers:
        ans: Answer = Answer()
        ans.id = answer.id
        ans.form_id = answer.form_id
        ans.answer_to = answer.answer_to
        ans.answer_text = answer.answer_text
        parsed_answers.append(ans)

    async with AsyncSession(autoflush=False, bind=engine) as db:
        q = insert(Answer).values(parsed_answers)
        await db.execute(q)
        await db.commit()


async def create_form(form: FormSchema, questions: list[QuestionSchema]) -> None:
    parsed_form: Form = Form()
    parsed_form.id = form.id
    parsed_form.created_by = form.created_by
    parsed_form.name = form.name
    parsed_form.description = form.description

    parsed_questions: list[Question] = []
    for question in questions:
        q = Question()
        q.id = question.id
        q.question_type = question.question_type
        q.choices = question.choices
        q.question_text = question.question_text
        q.question_image = question.question_image
        q.form_id = form.id

    async with AsyncSession(autoflush=False, bind=engine) as db:
        q = insert(Form).values(parsed_form)
        await db.execute(q)
        await db.commit()
