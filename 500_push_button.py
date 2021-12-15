from hax.button import Button

def push_button(button : Button):
    pass


def check():
    button = Button()
    push_button(button)

    if button.is_pushed:
        print(f"PASS: Button was pushed")
    else:
        print(f"FAIL: Button was not pushed")

if __name__=="__main__":
    check()