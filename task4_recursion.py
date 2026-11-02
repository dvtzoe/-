def count_digits(n: int) -> int:
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)


def power(base: int, exponent: int) -> int:
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)


def is_palindrome(text: str) -> bool:
    if len(text) < 2:
        return True
    return text[0] == text[-1] and is_palindrome(text[1:-1])
