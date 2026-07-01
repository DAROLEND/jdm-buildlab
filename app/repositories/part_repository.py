from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.parts import Part

class PartRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all(self) -> list[Part]:
        result = await self.session.execute(select(Part))
        return list(result.scalars().all())

    async def get_compatible_for_engine(self, engine_code: str) -> list[Part]:
        result = await self.session.execute(
            select(Part).where(Part.engine_code == engine_code)
        )
        return list(result.scalars().all())

    async def create(self, name: str, brand: str, category: str, engine_code: str, price_usd: int) -> Part:
        part = Part(name=name, brand=brand, category=category, engine_code=engine_code, price_usd=price_usd)
        self.session.add(part)
        await self.session.commit()
        await self.session.refresh(part)
        return part