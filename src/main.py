import os
import sys
import asyncio
# from queries.core import insert_data
from src.queries.orm import create_tables, insert_data, async_insert_data

sys.path.insert(1, os.path.join(sys.path[0], '..'))

create_tables()
# asyncio.run(async_insert_data())
