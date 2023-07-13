from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from login_user import login_user
from get_persons import get_persons

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
app.include_router(router=login_user)
app.include_router(router=get_persons)