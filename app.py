from fastapi import FastAPI
from routes.shoes import shoes

app = FastAPI()
app.include_router(shoes)