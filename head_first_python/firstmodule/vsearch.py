def search4vowels(phrase: str) -> set:
    """Return any vowels fround in a supplied phrase."""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


def search4letters(phrase: str, letters: str='aeiou') -> set:
    return set(letters).intersection(set(phrase))