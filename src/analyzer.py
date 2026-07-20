def count_requests(logs):
    return len(logs)

def count_status_codes(logs):

    status_counts = {}

    for log in logs:

        if log.status_code in status_counts:
            status_counts[log.status_code] += 1
        else:
            status_counts[log.status_code] = 1

    return status_counts

def count_paths(logs):

    path_counts = {}

    for log in logs:

        if log.path in path_counts:
            path_counts[log.path] += 1
        else:
            path_counts[log.path] = 1
    
    return path_counts

def analyze(logs):

    report = {
        "total_requests": count_requests(logs),
        "total_codes": count_status_codes(logs),
        "total_paths": count_paths(logs)
    }

    return report