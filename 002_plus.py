
def return_sum(a : int, b : int):
    pass


def check():
    tests = [
        (2, 2, 4),
        (0, 0, 0),
        (-1, 1, 0),
    ]
    for a, b, answer in tests:
        result = return_sum(a, b)
        if result == answer:
            print(f"PASS: ({a}, {b}) => ({result})")
        else:
            print(f"FAIL: ({a}, {b}) => ({result}) - expected {answer}")

if __name__=="__main__":
    check()