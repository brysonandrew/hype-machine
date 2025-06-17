from fastapi import APIRouter, Depends, Query
from openai import OpenAI
import logging
from utils.openai_client import get_openai_client

router = APIRouter()
logger = logging.getLogger("uvicorn.error")

@router.get("/hype")
def generate_hype(
    prompt: str = Query(..., description="Prompt to generate hype for"),
    client: OpenAI = Depends(get_openai_client),
):
    try:
        system_msg = "You're the Overhype Machine."
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_msg},
                {"role": "user", "content": prompt},
            ],
        )
        return {"hype": response.choices[0].message.content, "response": response}
    except Exception as e:
        logger.exception("Failed to generate hype")
        return {"error": "Something went wrong. The Hype Machine is recharging. " + str(e)}