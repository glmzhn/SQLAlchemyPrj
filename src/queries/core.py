from sqlalchemy import text, insert
from src.database import async_engine, sync_engine
from src.models import metadata_obj, workers_table


async def get_123():
    async with async_engine.connect() as conn:
        res = await conn.execute(text("SELECT 1,2,3 union select 4,5,6"))
        print(f'{res.first()=}')


def create_tables():
    sync_engine.echo = False
    metadata_obj.drop_all(sync_engine)
    metadata_obj.create_all(sync_engine)
    sync_engine.echo = True


def insert_data():
    with sync_engine.connect() as conn:
        # stat = """INSERT INTO workers (username) VALUES
        # ('BOBR'),
        # ('VOLK');"""
        stat = insert(workers_table).values(
            [
                {'username': 'Bobr'},
                {'username': 'Kurwa'}
            ]
        )
        conn.execute(stat)
        conn.commit()
