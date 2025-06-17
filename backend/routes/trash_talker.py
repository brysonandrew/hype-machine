from fastapi import APIRouter, Depends, Query

from openai import OpenAI
import os
from utils.openai_client import get_openai_client

router = APIRouter()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def get_prompt(situation: str, tone: str, subject: str) -> str:
    return f"""
You are a world-class trash talker, known for roasting subjects with perfect timing.
Tone: {tone.upper()}
Context: {situation.upper()}
Target: {subject}

Keep it short, sharp, and memorable.
"""


@router.get("/trash-talker")
def generate_trash(
    subject: str = Query(...),
    situation: str = Query(default="generic"),
    tone: str = Query(default="funny"),
    client: OpenAI = Depends(get_openai_client),
):
    prompt = get_prompt(situation, tone, subject)
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are the ultimate trash talk generator."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.9,
    )
    return {"trash_talk": response.choices[0].message.content.strip()}
