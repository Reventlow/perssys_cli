from datetime import datetime
from colorama import Fore, Style
import re
from rapidfuzz import fuzz


def strip_ansi(text):
    ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
    return ansi_escape.sub('', text)

def format_date(date_val):
    if not date_val:
        return "Ikke angivet"
    try:
        # Works if it's a datetime or already a string in 'YYYY-MM-DD'
        dt = datetime.strptime(str(date_val), "%Y-%m-%d")
        return dt.strftime("%d/%m-%Y")
    except Exception:
        return str(date_val)


def format_user_info(row):
    if not row:
        return None

    labels = [
        "Bruger", "Navn", "Email", "Mobil",
        "Afdeling", "Stilling", "Afdeling",
        "Startdato", "Slutdato", "Chef"
    ]

    values = [
        f"{row[0]}",
        f"{row[1]} {row[2]}",
        f"{row[3]}",
        f"{row[4]}",
        f"{row[5]}",
        f"{row[6]}",
        f"{row[7]}",
        f"{format_date(row[8])}",
        f"{format_date(row[9])}",
        f"{row[10]} ({row[11]})"
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
    pass

if __name__ == "__main__":
    main()
