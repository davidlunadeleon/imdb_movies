def clamp(val: int | float, min_val: int | float, max_val: int | float) -> int | float:
    return max(max(val, min_val), min(val, max_val))
