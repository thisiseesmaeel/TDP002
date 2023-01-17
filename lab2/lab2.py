def main():
   numbers = [1,2,3]
   numbers_reference = numbers
main()
-------------------------------------------------
def main():
    numbers = [1,2,3]
    numbers_reference = numbers.copy()
main()

#------------------------------------------------

def add_element(l,e):
    #add here
    l.append(e)
    
def main():
    numbers = [1,2,3]
    add_element(numbers,4)
main()


#----------------------------------------------------

def add_element(l,e):
    #add here
    l.append(e)
    
def main():
    numbers = [1,2,3]
    add_element(numbers.copy(), 4)
main()
