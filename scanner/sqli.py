patterns = [
    "' OR",
    "'--",
    "UNION",
    "SELECT",
    "DROP",
    "INSERT",
    "DELETE"
]


def detect_sqli(data):

    data = data.upper()

    for p in patterns:
        if p.upper() in data:
            return True

    return False
