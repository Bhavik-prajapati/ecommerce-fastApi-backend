from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import sentiment

app = FastAPI(title="Sentiment Analysis API")

# ✅ Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict to frontend origin here
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Include Sentiment Router
app.include_router(sentiment.router, prefix="/sentiment", tags=["Sentiment Analysis"])
