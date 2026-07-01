from fastapi import FastAPI
from routers import cars, parts

app = FastAPI(title="JDM BuildLab API")

app.include_router(cars.router)

app.include_router(cars.router)
app.include_router(parts.router)

@app.get("/")
async def root():
    return {"message": "Welcome to JDM BuildLab"}

@app.get("/health")
async def health():
    return {"status": "ok"}