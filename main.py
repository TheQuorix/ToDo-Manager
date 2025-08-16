from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database.database import Engine, Base
from routers import to_do


Base.metadata.create_all(bind=Engine)
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(to_do.router)