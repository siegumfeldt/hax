
def search_for_number(numbers : list[int], search_for : int):
    pass


def check():
    tests = [
        [(), 42, False],
        [(0, 42, 100, -1), 42, True],
    ]
    for numbers, search_for, answer in tests:
        result = search_for_number(search_for_number, search_for)
        if result == answer:
            print(f"PASS: {numbers} => {result}")
        else:
            print(f"FAIL: {numbers} => {result} (expected {answer})")

if __name__=="__main__":
    check()