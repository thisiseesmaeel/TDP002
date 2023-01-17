def process_integers(endVal, calc_func):
    nr_sum = 1
    for number in range(2, endVal+1):
        nr_sum = calc_func(nr_sum, number)
    return nr_sum

add_nr = lambda nr_sum, nr : nr_sum + nr
mul_nr = lambda nr_sum, nr : nr_sum * nr

print("Summan av alla naturliga tall upp till och med 512 är: " + str(process_integers(512, add_nr)))
print("Produkten av alla positiva heltal upp till och med 512 är: " + str(process_integers(512, mul_nr)))
