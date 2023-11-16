def arithmetic_progression(begin, step, end=None):
    """
    Generator for an arithmetic progression.

    Args:
    - begin: The starting element.
    - step: The difference between consecutive elements.
    - end: The final element.
    """
    current = begin
    while end is None or current < end:
        yield current
        current += step