from fastapi import APIRouter, Depends, Query

from openai import OpenAI
import os
from utils.openai_client import get_openai_client

router = APIRouter()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def get_prompt(
    target: str,
    context: str,
    tone: str
) -> str:
    return f"""
You are a world-class trash talker, known for roasting subjects with perfect timing.
Tone: {tone.upper()}
Context: {context.upper()}
Target: {target}

Keep it short, sharp, and memorable.

Use the Target text in the sentence.
"""


@router.get("/trash-talk")
def trash_talk(
    target: str = Query(...),
    context: str = Query(default="generic"),
    tone: str = Query(default="funny"),
    client: OpenAI = Depends(get_openai_client),
):
    prompt = get_prompt(context, tone, target)
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are the ultimate trash talk generator."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.9,
    )
    return {"trash_talk": response.choices[0].message.content.strip()}
