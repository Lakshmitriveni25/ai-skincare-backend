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

    products = {
        "oily": {
            "acne": {
                "Cleanser": {
                    "name": "CeraVe SA Cleanser",
                    "image": "https://m.media-amazon.com/images/I/71l0+6+EJFL._SL1500_.jpg",
                    "link": "https://www.amazon.com/dp/B00U1YCRD8"
                },
                "Moisturizer": {
                    "name": "Neutrogena Hydro Boost Water Gel",
                    "image": "https://m.media-amazon.com/images/I/61y6ZB+3XPL._SL1500_.jpg",
                    "link": "https://www.amazon.com/dp/B00NR1YQHM"
                },
                "Sunscreen": {
                    "name": "La Roche-Posay Anthelios SPF 50",
                    "image": "https://m.media-amazon.com/images/I/61o7u6L+4LL._SL1500_.jpg",
                    "link": "https://www.amazon.com/dp/B002CML1VG"
                }
            },
            "pigmentation": {
                "Cleanser": {
                    "name": "Cetaphil Brightening Cleanser",
                    "image": "https://m.media-amazon.com/images/I/61z5W5W+6bL._SL1500_.jpg",
                    "link": "https://www.amazon.com/dp/B09N3N9Z8K"
                },
                "Moisturizer": {
                    "name": "The Ordinary Niacinamide Cream",
                    "image": "https://m.media-amazon.com/images/I/51s9+z7Qh-L._SL1500_.jpg",
                    "link": "https://www.amazon.com/dp/B07BQN1H8K"
                },
                "Sunscreen": {
                    "name": "Supergoop Unseen SPF 50",
                    "image": "https://m.media-amazon.com/images/I/51k6A0+L1ML._SL1500_.jpg",
                    "link": "https://www.amazon.com/dp/B00J5WZ4E6"
                }
            }
        },
        "dry": {
            "acne": {
                "Cleanser": {
                    "name": "CeraVe Hydrating Cleanser",
                    "image": "https://m.media-amazon.com/images/I/71e6kR1rKAL._SL1500_.jpg",
                    "link": "https://www.amazon.com/dp/B01MSSDEPK"
                },
                "Moisturizer": {
                    "name": "CeraVe Moisturizing Cream",
                    "image": "https://m.media-amazon.com/images/I/71Z+6oX2hNL._SL1500_.jpg",
                    "link": "https://www.amazon.com/dp/B00TTD9BRC"
                },
                "Sunscreen": {
                    "name": "Aveeno Protect + Hydrate SPF 50",
                    "image": "https://m.media-amazon.com/images/I/61f6T9+uZVL._SL1500_.jpg",
                    "link": "https://www.amazon.com/dp/B07M5S1Y1K"
                }
            },
            "pigmentation": {
                "Cleanser": {
                    "name": "First Aid Beauty Cleanser",
                    "image": "https://m.media-amazon.com/images/I/61RzL1Z1X+L._SL1500_.jpg",
                    "link": "https://www.amazon.com/dp/B00N1LL62W"
                },
                "Moisturizer": {
                    "name": "Olay Vitamin C Cream",
                    "image": "https://m.media-amazon.com/images/I/71z+ZJ1ZPPL._SL1500_.jpg",
                    "link": "https://www.amazon.com/dp/B08N5WRWNW"
                },
                "Sunscreen": {
                    "name": "EltaMD UV Clear SPF 46",
                    "image": "https://m.media-amazon.com/images/I/61v2+0KJ7EL._SL1500_.jpg",
                    "link": "https://www.amazon.com/dp/B002MSN3QQ"
                }
            }
        }
    }

    result = products.get(skin, {}).get(concern)

    if not result:
        result = {
            "Cleanser": {"name": "Gentle Cleanser", "image": "", "link": ""},
            "Moisturizer": {"name": "Daily Moisturizer", "image": "", "link": ""},
            "Sunscreen": {"name": "SPF 50 Sunscreen", "image": "", "link": ""}
        }

    return {"recommendation": result}