db = [
('j', 'g'), ('a', 'u'), ('k', 'l'), ('o', 'i'),
('b', 's'),('b', 's'),('b', 's'),('b', 's'), ('@', '.'), ('p', 's'), ('o', 'e')
]

def quick_sort(input_list, sort_func = lambda x : x):
    lowerlist = []
    midlist = []
    higherlist = []
    if len(input_list) <= 1:
        return input_list
    else:
        ## pivot point, starts att first element in list
        midlist.append(input_list[0])
        
        #skips pivot point when sorting
        for entry in input_list[1:]:
            if sort_func(entry) <= sort_func(midlist[0]):
                lowerlist.append(entry)
            elif sort_func(entry) > sort_func(midlist[0]):
                higherlist.append(entry)
    return quick_sort(lowerlist, sort_func) + midlist + quick_sort(higherlist, sort_func)

print(quick_sort(db, lambda e : e[1]))


"""Skriv en funktion quicksort som tar en lista med element och en funktion för att specificera hur sorteringen ska gå till."""