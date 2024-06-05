from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from user_service import models, schemas, crud, auth
from user_service.database import SessionLocal, engine
import uvicorn

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.post("/token", response_model=schemas.Token)
def login_for_access_token(form_data: schemas.LoginForm, db: Session = Depends(get_db)):
    user = auth.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token = auth.create_access_token(user.id)
    return {"access_token": access_token, "token_type": "bearer"}

#if __name__ == "__main__":
#    uvicorn.run(app, host="0.0.0.0", port=8002)
