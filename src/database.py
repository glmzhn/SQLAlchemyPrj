from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from src.config import settings


sync_engine = create_engine(
    url=settings.database_url_psycopg,
    echo=True,
)

async_engine = create_async_engine(
    url=settings.database_url_asyncpg,
    echo=True,
)

session_factory = sessionmaker(sync_engine)
async_session_factory = async_sessionmaker(async_engine)


class Base(DeclarativeBase):
    pass
