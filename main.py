from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI
import os
import json
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

# ✅ CORS (keep this)
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

# ✅ Input model
class QuizInput(BaseModel):
    skin_type: str
    concern: str
    sensitivity: str

# ✅ OpenAI client (IMPORTANT: replace API key)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
@app.get("/")
def home():
    return {"message": "Backend running 🚀"}
# ✅ AI-based recommendation
@app.post("/recommend")
def recommend(data: QuizInput):
    try:
        prompt = f"""
        Give a SHORT skincare routine.

        Skin Type: {data.skin_type}
        Concern: {data.concern}
        Sensitivity: {data.sensitivity}

        Respond ONLY in JSON format like:
        {{
          "Cleanser": "...",
          "Moisturizer": "...",
          "Sunscreen": "..."
        }}
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",  # ✅ faster model
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        ai_text = response.choices[0].message.content

        # ✅ Convert AI text → JSON
        try:
            ai_json = json.loads(ai_text)
        except:
            # fallback if parsing fails
            ai_json = {
                "Cleanser": "Gentle Cleanser",
                "Moisturizer": "Daily Moisturizer",
                "Sunscreen": "SPF 50 Sunscreen"
            }

        return {"recommendation": ai_json}

    except Exception as e:
        return {
            "recommendation": {
                "Cleanser": "Error Cleanser",
                "Moisturizer": "Error Moisturizer",
                "Sunscreen": "Error Sunscreen"
            },
            "error": str(e)
        }