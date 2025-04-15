# Persys CLI Lookup Tool

This is a simple command-line tool to query user information from a Microsoft SQL Server `persys` table. It uses fuzzy matching to suggest possible users when no exact match is found.

## 📂 Project Structure

```
src/
├── main.py         # CLI logic, search, formatting, clipboard copy
├── persys.py       # Database access and user lookup logic
```

## 📦 Requirements

Install dependencies:

```bash
pip install pyodbc python-decouple colorama pyperclip rapidfuzz
```

## ⚙️ Environment Variables

Create a `.env` file in your project root (same level as `src/`) with the following:

```
DB_SERVER=your_server
DB_NAME=your_database
DB_USER=your_user
DB_PASSWORD=your_password
```

## 🧠 How It Works

1. The script first tries to find a user by exact `Brugernavn`.
2. If not found, it performs fuzzy matching on both `Brugernavn` and `Fornavn`.
3. If matches are found, it suggests alternatives like:
   ```
   - Sofie Jensen, soje, HR Services
   ```
4. If a user is found, their info is printed in color and copied to clipboard.

## ▶️ Running the Tool

```bash
python src/main.py
```

Then enter a username or first name when prompted.

## 🔄 Example Output

```
Enter username or firstname to search for: j.doo
User not found.

Did you mean:
- Jens Madsen, jmad, IT Support
- Jane Doe, jdoe, HR Services

Enter username or firstname to search for (or 'q' to quit):
```

If a match is found:

```
Bruger: 'jdoe'
Navn: 'Jane' 'Doe'
Email: 'jane.doe@example.com'
Mobil: '12345678'

Afdeling: 'HR'
Stilling: 'Consultant'
Afdeling: 'HR Services'
Startdato:  '2021-01-01'
Slutdato: '9999-12-31'
Chef: 'Hans Hansen' ('haha')
(Copied to clipboard)
```

## 🧽 Notes

- This tool is designed to run quickly in CLI environments.
- Clipboard copying works out-of-the-box on most systems.
