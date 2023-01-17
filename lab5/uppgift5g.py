def compose(F_a, F_b):
    return lambda x : F_a(F_b(x))

def multiply_five(n):
    return n * 5

def add_ten(x):
    return x + 10

if __name__ == "__main__":
    composition = compose(multiply_five, add_ten)
    another_composition = compose(add_ten,multiply_five)
# print(composition(3))
# print(another_composition(3))
