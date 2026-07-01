def validate_side(side: str):
    s = side.upper()
    if s not in ["BUY", "SELL"]:
        raise ValueError(f"bad side: {side}")
    return s

def validate_order_type(type: str):
    t = type.upper()
    if t not in ["MARKET", "LIMIT", "STOP_MARKET"]:
        raise ValueError(f"bad order type: {type}")
    return t

def validate_quantity(qty: float):
    if qty <= 0:
        raise ValueError("qty must be > 0")
    return qty
