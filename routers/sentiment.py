from fastapi import APIRouter
from transformers import pipeline
from models import ReviewList

router = APIRouter()

# Load the Hugging Face pipeline globally for reuse
sentiment_analyzer = pipeline("sentiment-analysis")

@router.get("/")
def home():
    return {"message": "Sentiment Analysis Backend Running"}

@router.post("/analyze")
def analyze_sentiment_bulk(review_list: ReviewList):
    results = sentiment_analyzer(review_list.reviews)
    return [
        {"review": review_text, "sentiment": result["label"], "confidence": result["score"]}
        for review_text, result in zip(review_list.reviews, results)
    ]
