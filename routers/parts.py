from fastapi import APIRouter, Depends
from typing import Annotated
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_db
from app.repositories.part_repository import PartRepository

router = APIRouter(prefix="/parts", tags=["Деталі"])

class PartCreate(BaseModel):
    name: str
    brand: str
    category: str
    engine_code: str
    price_usd: int

class PartOut(BaseModel):
    id: int
    name: str
    brand: str
    category: str
    engine_code: str
    price_usd: int

    class Config:
        from_attributes = True

DbDep = Annotated[AsyncSession, Depends(get_db)]

@router.get("/", response_model=list[PartOut])
async def list_parts(db: DbDep):
    repo = PartRepository(db)
    return await repo.get_all()

@router.post("/", response_model=PartOut, status_code=201)
async def create_part(data: PartCreate, db: DbDep):
    repo = PartRepository(db)
    return await repo.create(data.name, data.brand, data.category, data.engine_code, data.price_usd)