# Prompt Injection Shield

ML-based shield that detects prompt injection attacks on LLM chatbots.
Includes a Streamlit demo and a FastAPI service companies can plug in.

## Run (Windows)
```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python train.py
streamlit run app.py
```

## API
```
uvicorn main:app --reload
```
Open http://127.0.0.1:8000/docs and test /check with header `x-api-key: change-me`.

## Docker
```
docker build -t prompt-shield .
docker run -p 8000:8000 prompt-shield
```
