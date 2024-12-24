def mystery_8(a, b):
     """
    Returns a list of all characters in 'a' that match 'b'.

    Args:
        a (str): The input string.
        b (str): The character to search for.

    Returns:
        list: A list of all occurrences of 'b' in 'a'.
    """
    c = []
    while a:
        if b in a[0]:
            c.append(a[0])
        a = a[1:]
    return c


""" example 
 mystery_8("nagham", "a")
 output: ["a","a"]"""
