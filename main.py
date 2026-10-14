# FastAPI service: companies call /check before sending a message to their LLM
import joblib
from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Prompt Injection Shield API")
model = joblib.load("model.joblib")
API_KEY = "change-me"  # change this before sharing

class Msg(BaseModel):
    text: str

@app.post("/check")
def check(msg: Msg, x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")
    score = float(model.predict_proba([msg.text])[0][1])
    return {"is_attack": score >= 0.4, "score": round(score, 3)}
