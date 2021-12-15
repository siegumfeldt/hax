
def check_cases(f, cases):
    correct = 0
    for args, answer in cases:
        if is_correct(f, args, answer):
            correct += 1
    if correct == len(cases):
        print("Perfect!")    


def is_correct(f, args, answer):
    name = f.__name__
    arg_list = ', '.join(str(a) for a in args)
    try:
        result = f(*args)
    except Exception as e:
        print(f"FAIL: {name}({arg_list}) => {e}")
        return False
    if result == answer:
        print(f"PASS: {name}({arg_list}) => {result}")
        return True
    else:
        print(f"FAIL: {name}({arg_list}) => {result} (expected {answer})")
        return False

