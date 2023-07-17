from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from create_token import get_user, verify_password, encode_token, decode_token

login_user = APIRouter(prefix="/login", tags=["login"], responses={404: {"detail": "No encontrado"}})

@login_user.post("/")
def Login_user(form: OAuth2PasswordRequestForm = Depends()):   
    user = get_user(form.username)
    error = HTTPException(status_code=400, detail="Usuario invalido", headers={"WWW-Authenticate": "Bearer"})    
    
    if not user:
        raise error   
    if not verify_password(form.password, user.password):
        raise error
    
    token = encode_token(user.username)     
    return  {"access_token": token, "token_type": "bearer"}

@login_user.get("/")
def Get_user(response = Depends(decode_token)):    
    if response:
        return response
    
    error = HTTPException(status_code=401, detail="Token invalido", headers={"WWW-Authenticate": "Bearer"})      
    raise error  
    
 