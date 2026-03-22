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

    products = {
        "oily": {
            "acne": {
                "Cleanser": {
                    "name": "CeraVe SA Cleanser",
                    "image": "https://images.unsplash.com/photo-1585386959984-a4155224a1ad",
                    "link": "https://www.amazon.com/dp/B00U1YCRD8"
                },
                "Moisturizer": {
                    "name": "Neutrogena Hydro Boost",
                    "image": "https://images.unsplash.com/photo-1611930022073-b7a4ba5fcccd",
                    "link": "https://www.amazon.com/dp/B00NR1YQHM"
                },
                "Sunscreen": {
                    "name": "La Roche SPF 50",
                    "image": "https://images.unsplash.com/photo-1596755389378-c31d21fd1273",
                    "link": "https://www.amazon.com/dp/B002CML1VG"
                }
            },
            "pigmentation": {
                "Cleanser": {
                    "name": "Cetaphil Brightening Cleanser",
                    "image": "https://images.unsplash.com/photo-1585386959984-a4155224a1ad",
                    "link": "https://www.amazon.com"
                },
                "Moisturizer": {
                    "name": "Niacinamide Moisturizer",
                    "image": "https://images.unsplash.com/photo-1611930022073-b7a4ba5fcccd",
                    "link": "https://www.amazon.com"
                },
                "Sunscreen": {
                    "name": "Brightening SPF 50",
                    "image": "https://images.unsplash.com/photo-1596755389378-c31d21fd1273",
                    "link": "https://www.amazon.com"
                }
            }
        },
        "dry": {
            "acne": {
                "Cleanser": {
                    "name": "CeraVe Hydrating Cleanser",
                    "image": "https://images.unsplash.com/photo-1585386959984-a4155224a1ad",
                    "link": "https://www.amazon.com"
                },
                "Moisturizer": {
                    "name": "Ceramide Cream",
                    "image": "https://images.unsplash.com/photo-1611930022073-b7a4ba5fcccd",
                    "link": "https://www.amazon.com"
                },
                "Sunscreen": {
                    "name": "Hydrating SPF 50",
                    "image": "https://images.unsplash.com/photo-1596755389378-c31d21fd1273",
                    "link": "https://www.amazon.com"
                }
            },
            "pigmentation": {
                "Cleanser": {
                    "name": "Cream Cleanser",
                    "image": "https://images.unsplash.com/photo-1585386959984-a4155224a1ad",
                    "link": "https://www.amazon.com"
                },
                "Moisturizer": {
                    "name": "Vitamin C Cream",
                    "image": "https://images.unsplash.com/photo-1611930022073-b7a4ba5fcccd",
                    "link": "https://www.amazon.com"
                },
                "Sunscreen": {
                    "name": "Glow SPF 50",
                    "image": "https://images.unsplash.com/photo-1596755389378-c31d21fd1273",
                    "link": "https://www.amazon.com"
                }
            }
        }
    }

    result = products.get(skin, {}).get(concern)

    if not result:
        result = {
            "Cleanser": {"name": "Gentle Cleanser", "image": "", "link": ""},
            "Moisturizer": {"name": "Daily Moisturizer", "image": "", "link": ""},
            "Sunscreen": {"name": "SPF 50", "image": "", "link": ""}
        }

    return {"recommendation": result}