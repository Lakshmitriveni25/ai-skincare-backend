from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
    "http://localhost:3000",
    "https://ai-skincare-frontend.vercel.app"
],
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

    # OILY SKIN
    if skin == "oily" and concern == "acne":
        return {
            "recommendation": {
                "Cleanser": "Salicylic Acid Cleanser",
                "Moisturizer": "Oil-Free Gel Moisturizer",
                "Sunscreen": "Matte SPF 50 Sunscreen"
            }
        }

    elif skin == "oily" and concern == "pigmentation":
        return {
            "recommendation": {
                "Cleanser": "Foaming Cleanser",
                "Moisturizer": "Lightweight Moisturizer",
                "Sunscreen": "Brightening SPF 50 Sunscreen"
            }
        }

    # DRY SKIN
    elif skin == "dry" and concern == "acne":
        return {
            "recommendation": {
                "Cleanser": "Hydrating Acne Cleanser",
                "Moisturizer": "Ceramide Rich Moisturizer",
                "Sunscreen": "Hydrating SPF 50 Sunscreen"
            }
        }

    elif skin == "dry" and concern == "pigmentation":
        return {
            "recommendation": {
                "Cleanser": "Gentle Hydrating Cleanser",
                "Moisturizer": "Vitamin C Moisturizer",
                "Sunscreen": "Brightening SPF 50 Sunscreen"
            }
        }

    # DEFAULT
    else:
        return {
            "recommendation": {
                "Cleanser": "Gentle Cleanser",
                "Moisturizer": "Daily Moisturizer",
                "Sunscreen": "Broad Spectrum SPF 50"
            }
        }