from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.cars import Car

class CarRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all(self) -> list[Car]:
        result = await self.session.execute(select(Car))
        return list(result.scalars().all())

    async def get_by_id(self, car_id: int) -> Car | None:
        return await self.session.get(Car, car_id)

    async def create(self, brand: str, model: str, engine_code: str, hp: int) -> Car:
        car = Car(brand=brand, model=model, engine_code=engine_code, hp=hp)
        self.session.add(car)
        await self.session.commit()
        await self.session.refresh(car)
        return car

    async def delete(self, car: Car) -> None:
        await self.session.delete(car)
        await self.session.commit()