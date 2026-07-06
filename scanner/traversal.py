patterns = [
    "../",
    "..\\",
    "/etc/passwd",
    "windows/system32"
]


def detect_traversal(data):

    data = data.lower()

    for p in patterns:
        if p in data:
            return True

    return False
