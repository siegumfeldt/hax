
def return_true():
    pass


def check():
    result = return_true()
    if result:
        print(f"PASS: Returned something truthy ({result})")
    else:
        print(f"FAIL: Returned something falsy ({result})")

if __name__=="__main__":
    check()