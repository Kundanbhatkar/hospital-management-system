# Hospital Management System (H.M.S)

This is a small Flask-based Hospital Management System project. It provides basic user authentication, doctor and patient management, and appointment booking functionality. The project uses MySQL as the database backend and SQLAlchemy as the ORM.

## Contributors

- Kundan Santosh Bhatkar
- Gourang Waikar
- Sanket Markad

## Quick setup (Windows PowerShell)

1. Clone the repository:

```powershell
git clone https://github.com/Kundanbhatkar/hospital-management-system.git
cd "hospital system"
```

2. Create and activate a virtual environment:

```powershell
python -m venv venv
.\venv\Scripts\Activate
```

3. Install dependencies:

```powershell
pip install -r requirements.txt
```

4. Configure database and run the app:

- Create a MySQL database named `hmdbms` and update `PROJECT/main.py` SQLALCHEMY_DATABASE_URI if necessary.

```powershell
python PROJECT/main.py
```

The development server runs at http://127.0.0.1:5000

---

Backup note: A backup branch named `backup/pre-reset-8c47079` was pushed before overwriting `main` on the remote. If you need the previous version, check that branch on GitHub.