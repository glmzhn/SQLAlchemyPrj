from src.database import sync_engine, session_factory, async_session_factory
from src.models import WorkersOrm, Base


class SyncOrm:
    @staticmethod
    def create_tables():
        Base.metadata.drop_all(sync_engine)
        sync_engine.echo = True
        Base.metadata.create_all(sync_engine)
        sync_engine.echo = True

    @staticmethod
    def insert_workers():
        with session_factory() as session:
            worker_bobr = WorkersOrm(username='Bobr')
            worker_volk = WorkersOrm(username='Volk')
            session.add_all([worker_bobr, worker_volk])
            session.commit()


class AsyncOrm:
    @staticmethod
    async def async_insert_workers():
        async with async_session_factory() as session:
            worker_bobr = WorkersOrm(username='Bobr')
            worker_volk = WorkersOrm(username='Volk')
            session.add_all([worker_bobr, worker_volk])
            await session.commit()
