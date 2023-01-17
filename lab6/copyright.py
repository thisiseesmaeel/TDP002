import sys
import os
import re


def add_copyright(copyright_path, dest_path, extension=None):
    print("Source path:", copyright_path)
    print("Destination:", dest_path)

    extension = input("\nWhich file types do you want changed? Enter to choose all files.\n")
    target_ext = input("\nDo you want to change the extension of the file at the end? Enter to keep the old extensions.\n")

    # Finds all files that the user wants to work with.
    main_files = []

    # If the destination is a folder
    if os.path.isdir(dest_path):
        # Add all actual files to the main_files list.
        if extension == "":
            main_files = [dest_path + "/" + f for f in os.listdir(dest_path) if os.path.isfile(dest_path + "/" + f)]
        else:
            main_files = [dest_path + "/" + f for f in os.listdir(dest_path) if os.path.isfile(dest_path + "/" + f) and os.path.splitext(f)[1] == extension]
    # If the destination is a file, add it to main_files.
    elif os.path.isfile(dest_path):
        if extension == "":
            main_files.append(dest_path)
        elif os.path.splitext(dest_path)[1] == extension:
            main_files.append(dest_path)

    else:
        print("Invalid path")

    # Grabs the copyright information from a specified file.
    copyright_info = ""
    if os.path.isfile(copyright_path):
        with open(copyright_path) as copyright_file:
            copyright_info = "\n" + copyright_file.read()

    # Loops through all file paths we want to work with.
    for file_path in main_files:
        # Opens the file path in read/write mode.
        with open(file_path, "r+") as file:
            # Stores all file data as a string.
            data = file.read()

            # Regex replaces all old copyright-sections with a new section with new information in it.
            data = re.sub("BEGIN COPYRIGHT(.|s)*?END COPYRIGHT", "BEGIN COPYRIGHT" + copyright_info + "\nEND COPYRIGHT", data)

            # Cleanses the old file of content.
            delete_content(file)

            # Write the file with new content.
            file.write(data)
            print("Wrote new copyright content to:", file_path)

    # Renames all files to the new extension, if one was specified.
    if target_ext != "":
        for file in main_files:
            try:
                os.rename(file, os.path.splitext(file)[0] + target_ext)
            except:
                print("Couldn't rename", file, "Maybe the name already exists, or you don't have permission.")

# Deletes all content from an opened file.
def delete_content(pfile):
    # Sets the pointer to beginning of file.
    pfile.seek(0)

    # Tries to get the file size down to 0 kb, cleansing it.
    pfile.truncate()


def try_arguments():
    # Loads all system arguments.
    args = sys.argv

    # Calls add_copyright using the copyright file path and the destination path.
    if len(args) == 3:
        add_copyright(args[1], args[2])

    else:
        print("Invalid arguments. Arguments are -copyright_path, -destination_path")


try_arguments()


## python3 copyright.py text_copyright.txt testfiles





"""I den här uppgiften ska ni lägga till copyright-information i källkodsfiler. Ni ska dessutom enkelt kunna byta ut copyright-informationen till en
annan ifall ni vill publicera koden under olika licensvilkor.

Skriv ett program som kan användas på alla era källkodsfiler för att infoga copyright-information i filen.
Informationen ska infogas mellan markörerna BEGIN COPYRIGHT och END COPYRIGHT.
Ifall dessa markörer inte finns i filen ska filen inte förändras.
Ifall markörerna förekommer på flera ställen i filen ska copyright-informationen infogas på varje plats i filen.
Ifall det redan finns information mellan markörerna i filen ska den informationen ersättas. 
Markörerna ska vara kvar i den resulterande filen så att ni senare kan använda samma program för att byta till annan information. 
Programmet ska acceptera två kommandoradsparametrar. Den ena ska vara en fil som innehåller copyright-informationen och 
den andra ska vara den fil eller katalog där informationen ska infogas. 
Ifall det är en katalog ska samtliga filer i katalogen påverkas. 
Programmet ska även acceptera en flagga för att bara en viss filändelse ska behandlas och en flagga för att ändra filändelsen på resultatfilen."""