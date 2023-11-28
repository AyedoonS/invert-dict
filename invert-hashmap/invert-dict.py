# INVERT DICT/HASHMAP PYTHON3

def invert_dict(h: dict) -> dict[list]:
    """
    Returns a dictionary for doing reverse lookups on H.

    (i.e., the keys and values of <h> are swapped)
    """

    inverted = {}  # <- to be returned
    for key in h:
        value = h[key]
        if isinstance(value, list):
            value = tuple(value)
        if value not in inverted:
            inverted[value] = [key]
        else:
            inverted[value] += [key]
    return inverted
