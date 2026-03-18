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
    skin = data.skin_type.lower()
    concern = data.concern.lower()
    sensitive = data.sensitivity.lower()

    routine = {}

    # Cleanser
    if skin == "oily":
        routine["Cleanser"] = "Salicylic Cleanser"
    elif skin == "dry":
        routine["Cleanser"] = "Hydrating Cleanser"
    else:
        routine["Cleanser"] = "Gentle Cleanser"

    # Serum
    if concern == "acne":
        routine["Serum"] = "Niacinamide Serum"
    elif concern == "pigmentation":
        routine["Serum"] = "Vitamin C Serum"
    elif concern == "wrinkles":
        routine["Serum"] = "Retinol Serum"
    else:
        routine["Serum"] = "Basic Serum"

    # Moisturizer
    if sensitive == "yes":
        routine["Moisturizer"] = "Fragrance-Free Moisturizer"
    elif skin == "oily":
        routine["Moisturizer"] = "Oil-Free Moisturizer"
    else:
        routine["Moisturizer"] = "Hydrating Moisturizer"

    return {
        "recommendation": routine
    }