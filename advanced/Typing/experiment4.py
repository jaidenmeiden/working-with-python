from typing import Dict, List, Tuple

def is_palindrome(value: str) -> bool:
    value = value.replace(" ", "").lower()
    return value == value[::-1]

def run(value: str):
    print(is_palindrome(value))

if __name__ == '__main__':
    run("ana")
    run("gregorio")
    run(777)