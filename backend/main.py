from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.promote import router as promote_router
from routes.melody import router as melody_router
from routes.trash_talk import router as trash_talk_router

app = FastAPI()

# Optional: CORS for local Nuxt dev or Vercel prod
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or restrict to ["https://your-vercel-site.com"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/health")
def health_check():
    return {"status": "ok"}


app.include_router(promote_router)
app.include_router(melody_router)
app.include_router(trash_talk_router)
