import re

from model import NginxLogEntry


def parse_log_line(line: str) -> NginxLogEntry:

    pattern = r'(\S+) .* \[(.*?)\] "(.*?)" (\d+) (\d+)'

    match = re.search(pattern, line)

    if not match:
        raise ValueError("Invalid log format")

    ip, timestamp, request, status_code, response_size = match.groups()

    method, path, protocol = request.split()

    return NginxLogEntry(
        ip=ip,
        timestamp=timestamp,
        method=method,
        path=path,
        status_code=int(status_code),
        response_size=int(response_size)
    )

#test
if __name__ == "__main__":

    line = '192.168.1.10 - - [18/Jul/2026:16:30:45 +0300] "GET /index.html HTTP/1.1" 200 1024'

    log = parse_log_line(line)

    print(log)