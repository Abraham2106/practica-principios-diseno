import uuid


def siguiente_folio() -> str:
    return uuid.uuid4().hex[:6]
