import os

current_folder = os.getcwd() ## Skriver ut nuvarande arbetskatalog

## Skriv ut korrekt mapp
def cd_root():
    global current_folder
    current_folder = os.getcwd() ## Nu går det att använda 'pwd'

def find_last_slash(text):
    for index in (range(len(text)-2, -1, -1)):
        if text[index] == '/':
            return index

def cd_path(path):
    global current_folder
    if path != "..":
        current_folder += (path + "/")
    elif path == ".." and current_folder != "/":
        current_folder = current_folder[:find_last_slash(current_folder)+1]
    
def pwd():
    print(current_folder)

def ls():
    for file in os.listdir(current_folder):
        print(str(file))
    
def cat(file):
    with open(current_folder + "/" + file,'r') as file:
        data = file.read()
    print(data)


def run_commando():
    while True:
        comm = input("command> ")
        command = comm.split()

        if len(command) > 0:
            if command[0] == "pwd":
                pwd()
            elif command[0] == "cd":
                if len(command) > 1:
                    cd_path(command[1])
                else:
                    cd_root()
            elif command[0] == "ls":
                ls()
            elif command[0] == "cat":
                cat(command[1])
            
if __name__ == "__main__":
    run_commando()
