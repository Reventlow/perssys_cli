from perssys import PerssysDB
from tools import format_user_info, suggest_similar_users, strip_ansi
from colorama import Fore, init
import pyperclip


init(autoreset=True)


def main():
    db = PerssysDB()
    all_users = db.get_all_users_for_fuzzy()

    while True:
        search_input = input("Enter username or firstname to search for (or 'q' to quit): ").strip()
        if search_input.lower() == 'q':
            break

        row = db.find_user(search_input)
        if row:
            formatted = format_user_info(row)
            print(formatted + "\n")
            pyperclip.copy(strip_ansi(formatted))
            print(Fore.YELLOW + "(Copied to clipboard)\n")
        else:
            print("User not found.")
            suggestions = suggest_similar_users(search_input, all_users)
            if suggestions:
                print("\nDid you mean:")
                for suggestion in suggestions:
                    print(Fore.CYAN + suggestion)
            else:
                print(Fore.RED + "No similar users found.\n")

if __name__ == "__main__":
    main()
