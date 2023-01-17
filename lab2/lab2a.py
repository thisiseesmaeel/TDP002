# def frame():
#     mening = str(input("Skriv något: " ))
#     stars = "*"
#     print(len(mening)*stars+stars*4)
#     print(stars, mening, stars)
#     print(len(mening)*stars+stars*4)
# frame()

# +++++++++++++++++++++++++++++++++++++++++++

# def triangle(triangle):
#     rader = triangle
#     # rader = int(input('tMata in ett heltal: '))
#     for i in range(0, rader):
#         print("*" * (2*i+1))

# triangle(3)
   
#++++++++++++++++++++++++++++++++++++++++++++++++

def flag(flag):
    flag_star = flag
    # flag_star = int(input('Mata in ett heltal: '))
    for i in range(0, 8):
        if i == 4:
            print()
        print("*" * (flag_star*10), "*" * (flag_star*10))
flag(2)

# +++++++++++++++++++++++++++++++++++++++++++++++++




    
