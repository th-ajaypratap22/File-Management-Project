from pathlib import Path
import os


def readfileandfolder():
    path = Path("")
    items = list(path.rglob("*"))
    for i, item in enumerate(items):
        print(f"{i+1} : {item}")


def createfile():
    try:
        readfileandfolder()
        name = input("Please Tell Your File Name :-")
        p = Path(name)
        if not p.exists():
            with open(p, "w") as fs:
                data = input("What You Want To Write In This File :-")
                fs.write(data)

            print(f"FILE CREATED SUCCESSFULLY ")
        else:
            print("This File Already Exist")
    except Exception as err:
        print(f"An Error Occured As {err}")


def readfile():
    try:
        readfileandfolder()
        name = input("Which File You Want To Read :-")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p, "r") as fs:
                data = fs.read()
                print(data)
            print("FILE READ SUCCESSFULLY")
        else:
            print("The File Does Not Exist")
    except Exception as err:
        print(f"An Error Occured As {err}")


def updatefile():
    try:
        readfileandfolder()
        name = input("Tell Which File You Want To Update :- ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("Press 1 For Changing The Name Of Your File")
            print("Press 2 For Overwriting The Data Of Your File")
            print("Press 3 For Appending Some Content In Your File")

            res = int(input("Tell Your Response :-"))

            if res == 1:
                name2 = input("Tell Your New File Name :- ")
                p2 = Path(name2)
                p.rename(p2)
                print("FILE RENAMED SUCCESSFULLY")

            elif res == 2:
                with open(p, "w") as fs:
                    data = input("Tell What You Want To Write This Will Overwrite The File :- ")
                    fs.write(data)
            elif res == 3:
                with open(p, "a") as fs:
                    data = input("Tell What You Want To append In The File :- ")
                    fs.write(data)
            else:
                print("INVALID RESPONSE")
        else:
            print("File Does Not Exist. Enter Correct File Name.")
    except Exception as err:
        print(f"An Error Occured As {err}")


def deletefile():
    try:
        readfileandfolder()
        name = input("Which File You Want To Delete :- ")
        p = Path(name)

        if p.exists() and p.is_file():
            os.remove(p)
            print("FILE DELETE SUCCESSFULLY")
        else:
            print("No Such File Exist ")
    except Exception as err:
        print(f"An Error Occured As {err}")


print("Press 1 for Creating a File")
print("Press 2 for Reading a File")
print("Press 3 for Updating a File")
print("Press 4 for Deleting a File")
check = int(input("PLEASE TELL YOUR RESPONSE :-"))
if check == 1:
    createfile()
elif check == 2:
    readfile()
elif check == 3:
    updatefile()
elif check == 4:
    deletefile()
