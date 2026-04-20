from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
import models, schemas, auth

router = APIRouter()


# DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ✅ REGISTER
@router.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    try:
        # check existing user
        existing = db.query(models.User).filter(
            (models.User.username == user.username) |
            (models.User.email == user.email)
        ).first()

        if existing:
            raise HTTPException(status_code=400, detail="User already exists")

        # create new user
        new_user = models.User(
            username=user.username,
            email=user.email,
            password=auth.hash_password(user.password)
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)   # ✅ important

        return {"message": "User registered successfully"}

    except Exception as e:
        print("REGISTER ERROR:", e)
        raise HTTPException(status_code=500, detail=str(e))


# ✅ LOGIN (username OR email)
@router.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    try:
        db_user = db.query(models.User).filter(
            (models.User.username == user.username) |
            (models.User.email == user.username)
        ).first()

        if not db_user or not auth.verify_password(user.password, db_user.password):
            raise HTTPException(status_code=401, detail="Invalid credentials")

        token = auth.create_token({"user_id": db_user.id})

        return {"access_token": token}

    except Exception as e:
        print("LOGIN ERROR:", e)
        raise HTTPException(status_code=500, detail=str(e))