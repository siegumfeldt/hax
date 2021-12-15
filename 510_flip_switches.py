from hax.switch import Switch

def flip_switches(switches : list[Switch]):
    pass


def check():
    tests = [
        [],
        [Switch(True)],
        [Switch(True), Switch(True),  Switch(True)],
        [Switch(False)],
        [Switch(False), Switch(False),  Switch(False)],
        [Switch(False), Switch(True),  Switch(False)],
    ]

    for switches in tests:
        flip_switches(switches)

        if all(switch.is_flipped for switch in switches):
            print(f"PASS: All switches flipped.")
        else:
            print(f"FAIL: Got {repr(switches)}.")

if __name__=="__main__":
    check()