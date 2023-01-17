
def add(n, m): return n + m


def partial(func_arg,val):
    return lambda x: func_arg(val, x)

if __name__ == "__main__":
    add_five = partial(add, 5)
    add_ten = partial(add,10)
    print(add_ten(5))
    print(add_five(3))
