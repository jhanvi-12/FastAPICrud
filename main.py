# This is a sample Python script.
from fastapi import FastAPI
from app.api.view import router
# app variable is an instance of fastAPI class.

app = FastAPI(title="FastAPI application with MongoDB.")
app.include_router(router)