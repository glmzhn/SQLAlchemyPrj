import os
import sys
from queries.core import SyncCore, AsyncCore
from queries.orm import SyncOrm, AsyncOrm

sys.path.insert(1, os.path.join(sys.path[0], '..'))

# SyncOrm.create_tables()
#
# SyncOrm.insert_workers()

SyncCore.select_workers()
