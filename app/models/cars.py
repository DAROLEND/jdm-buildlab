from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class Car(Base):
    __tablename__ = "cars"

    id: Mapped[int] = mapped_column(primary_key=True)
    brand: Mapped[str]
    model: Mapped[str]
    engine_code: Mapped[str]
    hp: Mapped[int]
