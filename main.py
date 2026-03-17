
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QuizInput(BaseModel):
    skin_type: str
    concern: str
    sensitivity: str

@app.get("/")
def home():
    return {"message": "Backend running 🚀"}

@app.post("/recommend")
def recommend(data: QuizInput):
    if data.skin_type == "oily" and data.concern == "acne":
        return {
            "cleanser": "Salicylic Cleanser",
            "serum": "Niacinamide Serum",
            "moisturizer": "Oil-Free Moisturizer"
        }
    return {"message": "Basic recommendation"}
