from fastapi import APIRouter, Depends, Query
from openai import OpenAI
import logging
from utils.openai_client import get_openai_client

router = APIRouter()
logger = logging.getLogger("uvicorn.error")


def get_prompt(target: str, context: str, tone: str) -> str:
    return f"""
You are a world-class promoter, known for hyping anything and everything.
Tone: {tone.upper()}
Context: {context.upper()}
Target: {target}

Keep it short, sharp, and memorable.
"""


@router.get("/promote")
def promote(
    target: str = Query(...),
    context: str = Query(default="generic"),
    tone: str = Query(default="funny"),
    client: OpenAI = Depends(get_openai_client),
):
    try:
        prompt = get_prompt(target, context, tone)
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
        return {
            "error": "Something went wrong. The Hype Machine is recharging. " + str(e)
        }
