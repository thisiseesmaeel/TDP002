
def insertion_sort(input_list, sort_func = lambda x : x):
    for i in range(1, len(input_list)):
        for j in range(i, 0, -1):
            ## From left to right, if current is less than or equal to anything in sorted, place before it and break.
            if sort_func(input_list[j]) < sort_func(input_list[j-1]):
                input_list[j],input_list[j-1] = input_list[j-1],input_list[j]
            else:
                break

db = [
('j', 'g'), ('a', 'u'), ('k', 'l'), ('o', 'i'),
('b', 's'), ('@', '.'), ('p', 's'), ('o', 'e')
]

insertion_sort(db, lambda e : e[0])
print(db)


"""Ofta är det bra att kunna sortera data så att det går snabbare att söka igenom den.
Skriv en funktion insertion_sort som tar en lista med element och en funktion för att specificera hur sorteringen ska gå till.
Information om hur den fungerar hittar ni här.

Precis som i förra uppgiften ska funktionen ta emot dels listan som ska sorteras samt ha möjlighet att ta emot en funktion för att jämföra två element."""