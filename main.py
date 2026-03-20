from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI
import os
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI()

# ✅ CORS Configuration
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

# ✅ Input Model
class QuizInput(BaseModel):
    skin_type: str
    concern: str
    sensitivity: str

# ✅ OpenAI Client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ✅ Health Check
@app.get("/")
def home():
    return {"message": "Backend running 🚀"}

# ✅ Recommendation API
@app.post("/recommend")
def recommend(data: QuizInput):
    try:
        prompt = f"""
        Suggest a skincare routine.

        Skin Type: {data.skin_type}
        Concern: {data.concern}
        Sensitivity: {data.sensitivity}

        Respond ONLY in VALID JSON format:
        {{
          "Cleanser": "short name",
          "Moisturizer": "short name",
          "Sunscreen": "short name"
        }}
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
        )

        ai_text = response.choices[0].message.content.strip()

        # ✅ Clean response (remove ```json if present)
        if ai_text.startswith("```"):
            ai_text = ai_text.replace("```json", "").replace("```", "").strip()

        # ✅ Convert to JSON
        try:
            ai_json = json.loads(ai_text)
        except Exception as parse_error:
            print("JSON Parse Error:", parse_error)
            print("AI Response:", ai_text)

            # fallback
            ai_json = {
                "Cleanser": "Gentle Cleanser",
                "Moisturizer": "Hydrating Moisturizer",
                "Sunscreen": "SPF 50 Sunscreen"
            }

        return {"recommendation": ai_json}

    except Exception as e:
        print("SERVER ERROR:", str(e))

        return {
            "recommendation": {
                "Cleanser": "Gentle Cleanser",
                "Moisturizer": "Hydrating Moisturizer",
                "Sunscreen": "SPF 50 Sunscreen"
            }
        }