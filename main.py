from typing import List
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI(title="Sentiment Analysis API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

sentiment_analyzer = pipeline("sentiment-analysis")

class Review(BaseModel):
    text: str

class ReviewList(BaseModel):
    reviews: List[str]

@app.get("/")
def home():
    return {"message": "Sentiment Analysis Backend Running"}

@app.post("/analyze")
def analyze_sentiment_bulk(review_list: ReviewList):
    results = sentiment_analyzer(review_list.reviews)
    return [
        {"review": review_text, "sentiment": result["label"], "confidence": result["score"]}
        for review_text, result in zip(review_list.reviews, results)
    ]
