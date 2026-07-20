from parser import parse_log_line

def read_logs(filepath: str):
    logs = []

    with open(filepath, "r") as file:
        for line in file:
            log = parse_log_line(line.strip())
            logs.append(log)
    return logs

#test
if __name__ == "__main__":

    logs = read_logs("./sample_logs/access.log")

    for log in logs:
        print(log)