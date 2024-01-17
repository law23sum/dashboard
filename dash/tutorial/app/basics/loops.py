def loop_types():
    def simple_for_loop():
        print("Simple for loop:")
        for n in range(1, 4):
            print(n)
        print('finished')

    def for_loop_with_continue():
        print("For loop skipping a number using continue:")
        for n in (1, 2, 3):
            if n == 2:
                continue
            print(n)
        print('finished')

    def for_loop_with_break():
        print("For loop stopping execution with break:")
        for n in (1, 2, 3):
            if n == 2:
                break
            print(n)
        print('finished')

    def for_loop_no_conditions():
        print("For loop without any conditions:")
        for n in (1, 2, 3):
            print(n)
        print('finished')

    def while_loop_example():
        print("While loop example:")
        n = 0
        while n < 3:
            n = n + 1
            print(n)
        print('finished')