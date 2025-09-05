from fastapi import Depends,HTTPException
from typing import Annotated # To connect session and dependecy function we need Annotated
from sqlalchemy.orm import Session
from app.database import get_session
from fastapi.security import OAuth2PasswordBearer
from app.auth import decode_token
from app.models.user_model import User

SessionDep = Annotated[Session, Depends(get_session)]

# Must match the mounted router path for token acquisition
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

def get_curr_user(token:Annotated[str,Depends(oauth2_scheme)],session:SessionDep):
    payload = decode_token(token)
    if not payload:
        raise HTTPException(status_code=401,detail="User not found")
    user = session.query(User).filter(User.email == payload.get("sub")).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user