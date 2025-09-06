from fastapi import APIRouter
from pydantic import BaseModel
from transformers import pipeline

# Initialize a larger, instruction-tuned model for better descriptions
generator = pipeline("text2text-generation", model="google/flan-t5-large")

router = APIRouter()

# Request body schema
class TitleRequest(BaseModel):
    title: str

@router.post("/generate")
async def generate_description(data: TitleRequest):
    title = data.title

    # Prepare input for the model
    input_text = f"Write a detailed, engaging, and creative product description for this product name : {title}"
    print(input_text)

    # Generate description
    result = generator(
        input_text,
        max_new_tokens=250,  # generate longer text
        do_sample=True,
        top_p=0.95,          # sampling for creativity
        temperature=0.7
    )

    print(result[0])
    description = result[0]['generated_text']


    return {
        "title": title,
        "description": description
    }
