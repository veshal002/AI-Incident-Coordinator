from pathlib import Path


LOG_FILE = Path("data/logs/authentication.log")


def search_logs(query: str) -> str:
    """
    Search enterprise log files for relevant entries.
    """

    if not LOG_FILE.exists():
        return "Log file not found."

    matches = []

    with open(LOG_FILE, "r") as file:

        for line in file:

            if query.lower() in line.lower():

                matches.append(line.strip())

    if not matches:
        return "No matching log entries found."

    return "\n".join(matches[:20])