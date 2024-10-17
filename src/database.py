import asyncio

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import URL, create_engine, text
from config import settings

sync_engine = create_engine(
    url=settings.database_url_psycopg,
    echo=True,
)

async_engine = create_async_engine(
    url=settings.database_url_asyncpg,
    echo=True,
)


async def get_123():
    async with async_engine.connect() as conn:
        res = await conn.execute(text("SELECT 1,2,3 union select 4,5,6"))
        print(f'{res.first()=}')

asyncio.run(get_123())
