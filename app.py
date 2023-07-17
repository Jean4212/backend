from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from login_user import login_user
from select_data import select
from insert_data import insert

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
app.include_router(router=login_user)
app.include_router(router=select)
app.include_router(router=insert)