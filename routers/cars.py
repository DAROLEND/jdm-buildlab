from fastapi import APIRouter, HTTPException, Depends
from typing import Annotated
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_db
from app.repositories.car_repository import CarRepository
from app.repositories.part_repository import PartRepository

router = APIRouter(prefix="/cars", tags=["Авто"])

class CarCreate(BaseModel):
    brand: str
    model: str
    engine_code: str
    hp: int

class CarOut(BaseModel):
    id: int
    brand: str
    model: str
    engine_code: str
    hp: int

    class Config:
        from_attributes = True

DbDep = Annotated[AsyncSession, Depends(get_db)]

@router.get("/", response_model=list[CarOut])
async def list_cars(db: DbDep):
    repo = CarRepository(db)
    return await repo.get_all()

@router.get("/{car_id}", response_model=CarOut)
async def get_car(car_id: int, db: DbDep):
    repo = CarRepository(db)
    car = await repo.get_by_id(car_id)
    if car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    return car

@router.post("/", response_model=CarOut, status_code=201)
async def create_car(data: CarCreate, db: DbDep):
    repo = CarRepository(db)
    return await repo.create(data.brand, data.model, data.engine_code, data.hp)

@router.delete("/{car_id}", status_code=204)
async def delete_car(car_id: int, db: DbDep):
    repo = CarRepository(db)
    car = await repo.get_by_id(car_id)
    if car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    await repo.delete(car)

@router.get("/{car_id}/compatible-parts")
async def get_compatible_parts(car_id: int, db: DbDep):
    car_repo = CarRepository(db)
    part_repo = PartRepository(db)
    car = await car_repo.get_by_id(car_id)
    if car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    parts = await part_repo.get_compatible_for_engine(car.engine_code)
    return parts