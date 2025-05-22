def random1():
    print()
    input1 = int(input('''ENTER THE STARTING NUMBER: '''))
    input2 = int(input('''ENTER THE ENDING NUMBER: '''))
    print()
    if input1 > input2:
        import random
        a2 = random.randint(input2, input1)
        print(a2)
    elif input1 < input2:
        import random
        a2 = random.randint(input1, input2)
        print(a2)
    elif input1 == input2:
        a2 = input1
        print(a2)
    return a2
