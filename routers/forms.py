from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

import database as db
from fastapi import APIRouter
from models import *
from schemas import *


router = APIRouter(
    prefix="/forms"
)


@router.get("/{id}")
async def get_form(id: int) -> JSONResponse:
    form: Form = await db.get_form(id)
    return JSONResponse(content=jsonable_encoder(form))


@router.post("")
async def answer_form(answers: list[AnswerSchema]) -> JSONResponse:
    await db.answer_form(answers)
    return JSONResponse(content=jsonable_encoder(True))


@router.post("/new")
async def create_form(form: FormSchema, questions: list[QuestionSchema]) -> JSONResponse:
    await db.create_form(form)
    return JSONResponse(content=jsonable_encoder(True))