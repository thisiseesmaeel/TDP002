import uppgift5f
import uppgift5g


def make_filter_map(func1,func2):
    ##  Skapar en lista utifrån func1 (en lista av udda tal från 1 till 10)
    filtered = uppgift5f.partial(filter, func1)
    ## Iterirar genom och exekverar func2
    mapped = uppgift5f.partial(map, func2)
    
    composed = uppgift5g.compose(mapped,filtered)
    
    composedlist = uppgift5g.compose(list,composed)

    return composedlist


process = make_filter_map(lambda x: x % 2 == 1, lambda x: x * x)

print(process(range(10)))
