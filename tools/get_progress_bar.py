from constants import len_progress_bar, progress_bar_symbol


def get_progress_bar(percent):
    if percent is None:
        return None
    count_symbols = compute_count_symbols_in_progress_bar(percent)

    if count_symbols is None:
        return None

    result = "["
    for i in range(count_symbols):
        result += progress_bar_symbol

    while len(result) != len_progress_bar + 1:
        result += '.'

    result += "]"
    return result


def compute_count_symbols_in_progress_bar(percent):
    if percent == 100:
        return len_progress_bar

    if percent < 0 or percent > 100:
        return None

    count_symbols = len_progress_bar * percent / 100
    return round(float(count_symbols))


def is_integer(n):
    try:
        return int(n) == float(n)
    except ValueError:
        return False
