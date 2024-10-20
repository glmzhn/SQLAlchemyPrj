from sqlalchemy import insert
from src.database import sync_engine
from src.models import workers_table


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
