from sqlalchemy import insert, select
from src.database import sync_engine, Base, async_engine
from src.models import workers_table, metadata_obj


class SyncCore:
    @staticmethod
    def create_tables():
        Base.metadata.drop_all(sync_engine)
        sync_engine.echo = True
        Base.metadata.create_all(sync_engine)
        sync_engine.echo = True

    @staticmethod
    def insert_workers():
        with sync_engine.connect() as conn:
            stat = insert(workers_table).values(
                [
                    {'username': 'Bobr'},
                    {'username': 'Kurwa'}
                ]
            )
            conn.execute(stat)
            conn.commit()

    @staticmethod
    def select_workers():
        with sync_engine.connect() as conn:
            query = select(workers_table)
            result = conn.execute(query)
            workers = result.all()
            for i in workers:
                print(f'Worker Number: {i}')


class AsyncCore:
    @staticmethod
    async def create_tables():
        async with async_engine.begin() as conn:
            await conn.run_sync(metadata_obj.drop_all)
            await conn.run_sync(metadata_obj.create_all)
