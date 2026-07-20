from reader import read_logs
from analyzer import analyze


def main():
    log_file = "./sample_logs/access.log"

    logs = read_logs(log_file)

    report = analyze(logs)

    print(report)


if __name__ == "__main__":
    main()