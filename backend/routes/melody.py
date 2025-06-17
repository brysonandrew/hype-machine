from fastapi import APIRouter, Depends
from openai import OpenAI
import logging
from utils.openai_client import get_openai_client

router = APIRouter()
logger = logging.getLogger("uvicorn.error")

@router.get("/melody")
def generate_melody(
    prompt: str,
    client: OpenAI = Depends(get_openai_client),
):
    try:
        system_msg = "You're a music assistant. Output a melody as a sequence of notes like: C4 quarter, D4 eighth, E4 quarter..."
        messages = [
            {"role": "system", "content": system_msg},
            {"role": "user", "content": prompt},
        ]
        response = client.chat.completions.create(model="gpt-4", messages=messages)
        return {
            "melody": response.choices[0].message.content.strip(),
            "response": response,
        }
    except Exception as e:
        logger.exception("Failed to make melody")
        return {"error": "Something went wrong. The Note maker is recharging. " + str(e)}