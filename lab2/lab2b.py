def create_shopping_list():
    list = ["Kurslitteratur", "Anteckningsblock", "Penna"]
    return list

def shopping_list(list):
    n=1
    for i in list:
        print(str(n)+".", i)
        n+=1

def shopping_add(list):
    add_item = input("Vad ska läggas till i listan: ")
    list.append(add_item)

def shopping_remove(list):
    remove_item = int(input("Vilken sak vill du ta bort ur listan? "))
    del list[remove_item-1]

def shopping_edit(list):
    vilken = int(input("vilken item vill du ändra på ")) -1
    edit_item = input("Vad ska det stå istället för " + list[vilken])
    list[vilken] = edit_item

  

def main():
    list = create_shopping_list()
    print("Välkommen till shoppinglistan, välj ett alternativ: ")
    alternativ = 6
    while alternativ != 5:
        
        print("1. Skriv ut en existerande lista")
        print("2. Lägg till ett föremål i listan")
        print("3. Ta bort ett föremål ur listan")
        print("4. Ändra ett föremål i listan")
        print("5. Avsluta")

        alternativ = int(input())
        if alternativ == 1:
            shopping_list(list)
        
        if alternativ == 2:
            shopping_add(list)
        
        if alternativ == 3:
            shopping_remove(list)
        
        if alternativ == 4:
            shopping_edit(list)
        
        if alternativ == 5:
            print("Hej då")

main()
