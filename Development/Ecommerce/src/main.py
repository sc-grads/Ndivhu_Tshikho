from fastapi import FastAPI
from views import auth

app = FastAPI()

app.include_router(auth.router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.main:app", host="127.0.0.1", port=8000, reload=True)
