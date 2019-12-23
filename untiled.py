import time
import struct
from typing import List, Any

from Scheduler import Scheduler
from processes import Process

scheduler = Scheduler()
scheduler.load_data_from_file()
scheduler.run_round_robin(10)








