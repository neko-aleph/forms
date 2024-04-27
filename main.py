from fastapi import FastAPI
from routers.forms import router as form_router

app = FastAPI()
app.include_router(form_router)
