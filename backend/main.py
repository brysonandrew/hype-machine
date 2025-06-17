from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routes.hype import router as hype_router

app = FastAPI()

@app.get("/api")
def hello_world():
    return {"message": "Hello World", "api": "Python"}

@app.get("/api/test")
def test():
    return {"message": "Test"}

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


app.include_router(hype_router)
