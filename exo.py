def est_pair(n):
    return n % 2 == 0

def convert_to_hour(minute: int) -> str:
    if not isinstance(minute, int):
        return "error"
    if minute < 0:
        return "error"
    hours = minute // 60
    minutes = minute % 60
    return f"{hours} hour(s) and {minutes} minute(s)"

def convert_list(minutes_list: list[int]) -> list[str]:
    return [convert_to_hour(minute) for minute in minutes_list]

