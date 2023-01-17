#! /usr/bin/env python3

def generate_list(func, nr_int):
    res_list = []
    for nr in range(1, nr_int+2):
        res_list.append(func(nr))
    return res_list

def mirror(x):
     return x

def stars(n):
     return '*' * n

print(generate_list(mirror, 4))
print(generate_list(stars, 5))


