from typing import Sequence

def get_range(number : int) -> Sequence[int]:
    """
    Return a list of consecutive numbers starting at zero and not including `number`
    """
    pass


def check():
    tests = [
        (0, ()),
        (1, (0,)),
        (5, (0, 1, 2, 3, 4)),
    ]
    for number, answer in tests:
        try:
            result = tuple(get_range(number))
        except Exception as e:
            print(f'FAIL: {number} => "{e}" - excepted {repr(answer)}')
            continue
        if result == answer:
            print(f"PASS: {number} => {repr(answer)}")
        else:
            print(f"FAIL: {number} => {repr(result)} - excepted {repr(answer)}")


if __name__=="__main__":
    check()