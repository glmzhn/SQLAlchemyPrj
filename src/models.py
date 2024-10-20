from sqlalchemy import Table, Column, Integer, String, MetaData
from database import Base
from sqlalchemy.orm import Mapped, MappedColumn

metadata_obj = MetaData()

workers_table = Table(
    'workers',
    metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('username', String)
)


class WorkersOrm(Base):
    __tablename__ = 'workers'

    id: Mapped[int] = MappedColumn(primary_key=True)
    username: Mapped[str]
