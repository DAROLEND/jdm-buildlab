from sqlalchemy.orm import Mapped, mapped_column
from app.models.cars import Base

class Part(Base):
    __tablename__ = "parts"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    brand: Mapped[str]
    category: Mapped[str]
    engine_code: Mapped[str]
    price_usd: Mapped[int]