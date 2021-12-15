
def calculate_sum(numbers : list[int]):
    pass


def check():
    tests = [
        [(), 0],
        [(-4, -3, -2, -1, 0, 1, 2, 3, 4), 0],
        [(0, 1, 2, 3, 4, 5, 6, 7, 8, 9), 45],
    ]
    for numbers, answer in tests:
        result = calculate_sum(numbers)
        if result == answer:
            print(f"PASS: {numbers} => {result}")
        else:
            print(f"FAIL: {numbers} => {result} (expected {answer})")

if __name__=="__main__":
    check()