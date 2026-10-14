FROM python:3.11-slim
WORKDIR /app
RUN pip install --no-cache-dir scikit-learn joblib fastapi uvicorn
COPY main.py model.joblib ./
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
