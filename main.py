# FastAPI service: companies call /check before sending a message to their LLM
import os
import joblib
from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Prompt Injection Shield API")
model = joblib.load("model.joblib")

# The API key is read from an environment variable (set it on Render).
API_KEY = os.environ.get("API_KEY", "change-me")


class Msg(BaseModel):
    text: str


@app.get("/")
def home():
    return {"status": "Prompt Injection Shield API is running", "docs": "/docs"}


@app.post("/check")
def check(msg: Msg, x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")
    score = float(model.predict_proba([msg.text])[0][1])
    return {"is_attack": score >= 0.5, "score": round(score, 3)}
