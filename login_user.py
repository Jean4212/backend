from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from create_token import get_user, verify_password, encode_token, decode_token

route_login = APIRouter(tags=["Login"], responses={404: {"detail": "No encontrado"}})

def http_error(code: int, message: str):
    return HTTPException(status_code=code, detail=message, headers={"WWW-Authenticate": "Bearer"})

@route_login.get("/user")
def current_user(response = Depends(decode_token)):    
    if response:
        return response     
      
    raise http_error(401, "Token invalido")  

@route_login.post("/login")
def login_user(form: OAuth2PasswordRequestForm = Depends()):   
    user = get_user(form.username)
    error = http_error(400, "Usuario invalido")    
    
    if not user:
        raise error   
    if not verify_password(form.password, user.password):
        raise error    
   
    return  {"access_token": encode_token(user.username), "token_type": "bearer"}
