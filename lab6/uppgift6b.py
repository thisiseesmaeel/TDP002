
def binary_search(input_list, search_value, search_func = lambda x : x):
    center = int((len(input_list)/2)+0.5) - 1 ## Equivalent to (inputlist // 2) for finding the center position

    if(center == -1):
        return "Not found!"
    if search_func(input_list[center]) == search_value:
        return input_list[center]
    ## If the center value is less than target, remove the last half of the search range.
    elif search_func(input_list[center]) < search_value:
        return binary_search(input_list[center+1:], search_value, search_func)
    ## If the center value is bigger than target, remove the first half of the search range.
    elif search_func(input_list[center]) > search_value:
        return binary_search(input_list[:center], search_value, search_func)

people = [{'name': 'Pontus', 'age': 30},
          {'name': 'Sara', 'age': 20},
          {'name': 'Xavier', 'age': 19}]

print(binary_search(people, "Pontus", lambda e: e['name']))



"""Binärsökning fungerar om mängden ni söker i är sorterad och på så sätt att ni hela tiden jämför det eftersökta
 elementet med elementet på mittenpositionen i sökmängden,därefter begränsar ni sökmängden beroende på utfallet av jämförelsen.

Skriv en funktion binary_search som söker igenom en lista (haystack) efter ett specifikt värde (needle).
Funktionen ska dessutom ha möjlighet att ta ett tredje argument med en funktion för att specificera 
hur jämförelsen av två element i listan ska gå till."""