patterns = [
    "<script>",
    "javascript:",
    "onerror=",
    "onload="
]


def detect_xss(data):

    data = data.lower()

    for p in patterns:
        if p in data:
            return True

    return False
