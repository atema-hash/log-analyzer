from dataclasses import dataclass
from datetime import datetime

@dataclass
class NginxLogEntry:
    ip:str
    timestamp: datetime
    method: str
    path:str
    status_code: int
    response_size: int