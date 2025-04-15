# PersSys CLI

A cross-platform command-line tool for querying user information from a Microsoft SQL Server database via the `persys` table. Designed for use across macOS, Windows, and Linux using `python-tds` (no ODBC dependency).

---

## 🔧 Requirements
Install Python 3.8+ and run:

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage
Run the main script from terminal:

```bash
python src/main.py
```

You will be prompted to search for a user by **username** or **first name**. If no exact match is found, fuzzy suggestions will be offered.

The output is color-formatted in the terminal, but plain text is automatically copied to your clipboard for easy pasting.

---

## 💻 Setup Instructions
Clone the repository and set up a virtual environment:

```bash
git clone https://github.com/Reventlow/perssys_cli.git
cd perssys_cli
```

### 🪟 Windows
```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
python src\main.py
```

### 🍏 macOS / 🐧 Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/main.py
```

---

## 📂 Project Structure
```
src/
├── main.py        # CLI loop and interaction
├── perssys.py     # Database access via pytds
├── tools.py       # Helper functions (formatting, fuzzy match, clipboard clean)
```

---

## 📄 .env Configuration
Create a `.env` file at the root level:

```env
DB_SERVER=server_info
DB_PORT=1433
DB_NAME=database_name
DB_USER=your_username
DB_PASSWORD=your_password
```

---

## 📦 requirements.txt
```
colorama==0.4.6
pyperclip==1.9.0
python-decouple==3.8
python-tds==1.16.1
RapidFuzz==3.13.0
```

---

## 📝 License
MIT License  
Copyright (c) 2025 Reventlow
