from sys import exit

def start():
    # Finally figured how to make my printed stuff appear flush when using multi-line print...
    print("""Listen ye. You must solve two riddles.
    And they are both two-parters!
    So good luck.""")
    test_1()

def test_1():
    print("Okay riddle one, part one: Is it 'okay' eat dinner in front of the television? Type 'yes' or 'no' please.")

    while True:
        choice1 = input("> ")
        if choice1 == "yes":
            print("Sure it is. Now part two:")
            money_test_2()
        elif choice1 == "no":
            print("Okay, that's fine, that's admirable maybe? I mean, I think I used to feel that way.")
            test_2()

def test_2():
    print("Okay checking on this--just type 'yes' please.")
    choice2 = input("> ")
    if choice2 == "yes":
        print("Nice.")
        exit(0)
    else:
        print("That's not 'yes'!")
        exit(0)

start()
