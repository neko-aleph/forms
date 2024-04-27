from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import ARRAY


class Base(DeclarativeBase):
    ...


class Answer(Base):
    __tablename__: str = 'answers'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    answer_to: Mapped[int] = mapped_column(ForeignKey("questions.id"))
    answer_text: Mapped[str] = mapped_column(nullable=False)


class Question(Base):
    __tablename__: str = 'questions'
    id: Mapped[int] = mapped_column(primary_key=True)
    question_type: Mapped[str] = mapped_column(nullable=False)
    choices: Mapped[list[str]] = mapped_column(ARRAY(String))
    question_text: Mapped[str] = mapped_column()
    question_image: Mapped[str] = mapped_column()
    answers: Mapped[list[Answer]] = relationship()
    form_id: Mapped[int] = mapped_column(ForeignKey("forms.id"))


class Form(Base):
    __tablename__: str = 'forms'
    id: Mapped[int] = mapped_column(primary_key=True)
    created_by: Mapped[int] = mapped_column(ForeignKey("users.id"))
    name: Mapped[str] = Column(String, nullable=False)
    description: Mapped[str] = Column(String)
    questions: Mapped[list[Question]] = relationship()


class User(Base):
    __tablename__: str = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)
    forms: Mapped[list[Form]] = relationship()
