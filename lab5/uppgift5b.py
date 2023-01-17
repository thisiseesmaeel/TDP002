db = [
{'name': 'examiner', 'position': 'assistant'},
{'name': 'Daniel', 'position': 'assistant'},
{'name': 'Samuel', 'position': 'examiner'},
{'name': 'Simon', 'position': 'assistant'}
]

def dbsearch(db, field,value):
    returnlist = []

    for entry in db:
        for key,val in entry.items():
            if val == value and key == field:
                returnlist.append(entry)

    return returnlist

print (dbsearch (db , 'position', 'assistant'))
print (dbsearch (db , 'position', 'examiner'))
