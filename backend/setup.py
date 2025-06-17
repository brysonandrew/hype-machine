import subprocess
import sys

packages = [
    "fastapi",
    "uvicorn[standard]",
    "openai",
    "python-dotenv",
    "httpx"
]

def install():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
    subprocess.check_call([sys.executable, "-m", "pip", "install"] + packages)

if __name__ == "__main__":
    install()