from fastapi import FastAPI

app = FastAPI(
    title="JDM BuildLab",
    description="API тюнінг-конфігуратора японських авто",
    version="0.1.0",
)


@app.get("/")
async def root():
    return {"message": "JDM BuildLab API is running 🏎️"}
