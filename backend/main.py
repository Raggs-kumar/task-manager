from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# import your modules
from database import engine
import models

from routes import user, task   # make sure this path matches your folder

# create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# ✅ CORS configuration
origins = [
    "http://localhost:8081",  # frontend URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ include routers
app.include_router(user.router)
app.include_router(task.router)

# ✅ root route
@app.get("/")
def root():
    return {"message": "API running"}