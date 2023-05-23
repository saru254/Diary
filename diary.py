import colorama
from colorama import Fore, Style

def add_entry():
    entry = input("write your diary entry: ")
    with open("diary.txt", "a") as f:
        f.write(entry + "/n")
    print(Fore.BLUE + "Entry added successfully!" +Style.RESET_ALL)
    
def read_entries():
    try:
        with open("diary.txt", "r") as f:
            entries = f.readlines()
        if not entries:
            print(Fore.GREEN + "No entries found." + Style.RESET_ALL)
        else:
            print(Fore.CYAN + "DIiary entries:" + Style.RESET_ALL)
            for entry in entries:
                print(entry.strip())
    except FileNotFoundError:
        print(Fore.LIGHTMAGENTA_EX + "no diary entries found." + Style.RESET_ALL)
        
def menu():
    print(Fore.BLUE + "=== STLYLISH DIARY===" + Style.RESET_ALL)
    print("1. Add Diary Entry")
    print("2. Read Diary entries")
    print("3. Exit")
    
while True:
    menu()
    choice = input("Enter your choice (1-3): ")
    if choice =="1":
        add_entry()
    elif choice =="2":
        read_entries()
    elif choice == "3":
        print(Fore.RED + "Exiting the stylish Diary..." + Style.RESET_ALL)
        break
    else:
        print(Fore.YELLOW + "Invalid choice.Please try again" + Style.RESET_ALL)
        
    print("Goodbye!")