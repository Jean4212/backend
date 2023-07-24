from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

@app.get("/", tags=["Home"])
def home():
    return {"detail": "API is ready"}

from login_user import route_login
from employee import route_staff
from schedule import route_calendar
from config_admin import route_admin

app.include_router(router=route_login)
app.include_router(router=route_staff)
app.include_router(router=route_calendar)
app.include_router(router=route_admin)