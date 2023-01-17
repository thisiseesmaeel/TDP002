def linear_search(input_list, search_value, search_func = lambda x : x):
    for val in input_list:
        if search_func(val) == search_value:
            return val

dict_list = [{'title': 'Fel', 'actress': 'Helt fel', 'score': 5},
             {'title': 'Raise your voice', 'actress': 'Hilary Duff', 'score': 10},
             {'title': 'Rätt?', 'actress': 'Inte rätt', 'score': 15}]

print(linear_search(dict_list, 10, lambda e: e['score']))


"""Linjärsökning är den simplaste formen av sökning ni kan tänka er. Det går helt enkelt ut på att ni börjar söka från början 
av listan och slutar när ni hittar elementet ni letar efter eller kommer till slutet av listan.
Linjärsökning har fördelen att den även fungerar för osorterad data.

Skriv en funktion linear_search som söker igenom en lista (haystack) efter ett specifikt värde (needle).
Funktionen ska dessutom ha möjlighet att ta ett tredje argument med en funktion för att specificera hur jämförelsen ska gå till."""
