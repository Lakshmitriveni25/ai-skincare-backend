from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS
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

# Input model
class QuizInput(BaseModel):
    skin_type: str
    concern: str
    sensitivity: str

# Health check
@app.get("/")
def home():
    return {"message": "Backend running 🚀"}

# 🔥 FINAL LOGIC
@app.post("/recommend")
def recommend(data: QuizInput):
    skin = data.skin_type.lower()
    concern = data.concern.lower()

    print("INPUT:", skin, concern)  # for debugging

    recommendations = {
        "oily": {
            "acne": {
                "Cleanser": "Salicylic Acid Cleanser",
                "Moisturizer": "Oil-Free Gel Moisturizer",
                "Sunscreen": "Matte SPF 50 Sunscreen"
            },
            "pigmentation": {
                "Cleanser": "Foaming Brightening Cleanser",
                "Moisturizer": "Niacinamide Gel Moisturizer",
                "Sunscreen": "Brightening SPF 50 Sunscreen"
            }
        },
        "dry": {
            "acne": {
                "Cleanser": "Hydrating Acne Cleanser",
                "Moisturizer": "Ceramide Rich Moisturizer",
                "Sunscreen": "Hydrating SPF 50 Sunscreen"
            },
            "pigmentation": {
                "Cleanser": "Cream-Based Gentle Cleanser",
                "Moisturizer": "Vitamin C Moisturizer",
                "Sunscreen": "Glow SPF 50 Sunscreen"
            }
        }
    }

    # Get result safely
    result = recommendations.get(skin, {}).get(concern)

    if not result:
        result = {
            "Cleanser": "Gentle Cleanser",
            "Moisturizer": "Daily Moisturizer",
            "Sunscreen": "SPF 50 Sunscreen"
        }

    return {"recommendation": result}