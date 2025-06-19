from fastapi import FastAPI

from routes.parser import router as parser_router

app = FastAPI()
app.include_router(parser_router)