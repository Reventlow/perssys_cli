from persys import PersysDB
from colorama import Fore, Style, init
import pyperclip
from rapidfuzz import fuzz

init(autoreset=True)

def format_user_info(row):
    if not row:
        return None

    labels = [
        "Bruger", "Navn", "Email", "Mobil",
        "Afdeling", "Stilling", "Afdeling",
        "Startdato", "Slutdato", "Chef"
    ]
    
    values = [
        f"'{row[0]}'",
        f"'{row[1]}' '{row[2]}'",
        f"'{row[3]}'",
        f"'{row[4]}'",
        f"'{row[5]}'",
        f"'{row[6]}'",
        f"'{row[7]}'",
        f"'{row[8]}'",
        f"'{row[9]}'",
        f"'{row[10]}' ('{row[11]}')"
    ]

    output = ""
    for label, value in zip(labels, values):
        output += f"{label}: {Fore.CYAN}{value}{Style.RESET_ALL}\n"
    return output.strip()

def suggest_similar_users(input_str, users, limit=3):
    matches = []
    for u in users:
        brugernavn, fornavn, efternavn, afdeling = u
        score_username = fuzz.WRatio(input_str, brugernavn)
        score_fornavn = fuzz.WRatio(input_str, fornavn)
        best_score = max(score_username, score_fornavn)
        matches.append((best_score, f"- {fornavn} {efternavn}, {brugernavn}, {afdeling}"))

    matches.sort(reverse=True, key=lambda x: x[0])
    return [match[1] for match in matches[:limit] if match[0] > 60]

def main():
    db = PersysDB()
    all_users = db.get_all_users_for_fuzzy()

    while True:
        search_input = input("Enter username or firstname to search for (or 'q' to quit): ").strip()
        if search_input.lower() == 'q':
            break

        row = db.find_user(search_input)
        if row:
            formatted = format_user_info(row)
            print(formatted + "\n")
            pyperclip.copy(formatted)
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
