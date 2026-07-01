# JDM BuildLab

API тюнінг-конфігуратора японських авто — наскрізний проєкт FastAPI плану.

## Стек
- FastAPI, PostgreSQL, SQLAlchemy 2.0 (async), Alembic, Pydantic v2, JWT, pytest, Docker

## Структура
```
app/
├── core/          # конфіг, безпека
├── models/        # SQLAlchemy моделі
├── schemas/       # Pydantic схеми
├── routers/       # FastAPI роутери
├── services/      # бізнес-логіка
└── repositories/  # запити до БД
```

## Старт (Фаза 6+)
```bash
uvicorn app.main:app --reload
```

## MVP ендпоінти
- GET  /cars — каталог авто
- GET  /parts — каталог запчастин
- POST /builds — створити білд
- GET  /builds/{id}/compatibility — перевірити сумісність
