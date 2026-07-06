import time

clients = {}

LIMIT = 5
WINDOW = 60


def allow_request(ip):

    now = time.time()

    if ip not in clients:
        clients[ip] = []

    clients[ip] = [
        t for t in clients[ip]
        if now - t < WINDOW
    ]

    if len(clients[ip]) >= LIMIT:
        return False

    clients[ip].append(now)

    return True
