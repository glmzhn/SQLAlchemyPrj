import datetime
from typing import Annotated
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, text
from database import Base, str_256
from sqlalchemy.orm import Mapped, mapped_column
import enum

metadata_obj = MetaData()

workers_table = Table(
    'workers',
    metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('username', String)
)

intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime.datetime, mapped_column(server_default=text('now()'))]
updated_at = Annotated[datetime.datetime, mapped_column(server_default=text('now()'),
                                                        onupdate=datetime.datetime.now(datetime.UTC))]


class WorkersOrm(Base):
    __tablename__ = 'workers'

    id: Mapped[intpk]
    username: Mapped[str_256]


class Workload(enum.Enum):
    parttime = 'parttime'
    fulltime = 'fulltime'


class ResumesOrm(Base):
    __tablename__ = 'resumes'

    id: Mapped[intpk]
    title: Mapped[str_256]
    salary: Mapped[int | None]
    workload: Mapped[Workload]
    worked_id: Mapped[int] = mapped_column(ForeignKey('workers.id', ondelete='CASCADE'))
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
