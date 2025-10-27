# app.py
import os
import time
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from collections import deque
from datetime import datetime
from textblob import TextBlob

app = FastAPI(title="AI Sentiment Effect Detector")

# Simple cache for last 5 predictions
cache = deque(maxlen=5)

class TextInput(BaseModel):
    text: str

@app.post("/analyze")
def analyze_text(data: TextInput):
    start_time = time.time()
    
    try:
        # Use TextBlob for sentiment analysis
        blob = TextBlob(data.text)
        polarity = blob.sentiment.polarity
        
        # Convert polarity to sentiment labels
        if polarity > 0.1:
            sentiment = "positive"
        elif polarity < -0.1:
            sentiment = "negative"
        else:
            sentiment = "neutral"
        
        cache.append({"text": data.text, "sentiment": sentiment, "polarity": polarity})
        
        avg_time = round((time.time() - start_time), 3)
        print(f"[{datetime.now()}] Text: {data.text} → Sentiment: {sentiment} (polarity: {polarity:.3f}) | Response time: {avg_time}s")

        return {
            "sentiment": sentiment,
            "polarity": round(polarity, 3),
            "confidence": round(abs(polarity), 3)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Sentiment analysis failed: {str(e)}")

@app.get("/cache")
def get_cache():
    """Get the last 5 analyzed texts from cache"""
    return {"cache": list(cache)}
