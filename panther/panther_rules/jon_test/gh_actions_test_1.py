import datetime


def rule(event):
    return event.get("status") == 200 and "admin-panel" in event.get(request)


def title(event):
    return f"Successful admin panel login detected from {event.get('remoteAddr')}"


def dedup(event):
    return event.get("remoteAddr")
