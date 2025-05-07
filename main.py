from fastapi import FastAPI
from database import Base, engine
from routres import users, resaturants, dishes

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(resaturants.router)
app.include_router(dishes.router)
