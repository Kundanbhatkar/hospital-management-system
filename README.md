# Hospital Management System (H.M.S)

This is a small Flask-based Hospital Management System project. It provides basic user authentication, doctor and patient management, and appointment booking functionality. The project uses MySQL as the database backend and SQLAlchemy as the ORM.

## Repository structure

- `PROJECT/` - Flask app
  - `main.py` - Application entry point
  - `templates/` - Jinja2 HTML templates
  - `static/` - Static files (CSS, images)
- `hms.sql` - SQL dump to create the database and sample data
- `requirements.txt` - Python dependencies

## Prerequisites

- Python 3.8+ installed
- MySQL (or MariaDB) server running locally
- (Optional) Git and GitHub account for pushing/pulling the repo

## Quick setup (Windows PowerShell)

1. Clone the repository (if you haven't already):

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

4. Create the database:

- Create a database named `hmdbms` in your MySQL server, or import the provided SQL dump (`hms.sql`) using a client like `mysql` or `phpMyAdmin`.

Example using command line (adjust username/password as needed):

```powershell
mysql -u root -p
# then in mysql client:
# CREATE DATABASE hmdbms;
# USE hmdbms;
# SOURCE path/to/hms.sql;
```

5. Configure the database URI (if necessary):

The app uses the SQLAlchemy URI configured in `PROJECT/main.py`:

```python
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost/hmdbms'
```

Edit this line to include your MySQL username and password if different.

6. Run the application:

```powershell
python PROJECT/main.py
```

The development server will start on http://127.0.0.1:5000. Open that URL in your browser to preview the app.

## Notes & Security

- `app.secret_key` is currently hardcoded in `PROJECT/main.py` for convenience. For production use, set a secure secret key via environment variable and avoid committing secrets in source control.
- Passwords in the database are not consistently hashed in this project. Consider using `werkzeug.security.generate_password_hash` and `check_password_hash` for password storage and verification.
- The Flask development server is not suitable for production. Use a production WSGI server (e.g., Gunicorn, uWSGI) behind a reverse proxy.

## Common tasks

- Start dev server: `python PROJECT/main.py`
- Run database check endpoint: visit `http://127.0.0.1:5000/test`

## Contributing

If you'd like me to make further UI improvements, convert to Bootstrap 5, add automated tests, or harden authentication, tell me and I can implement them and push the changes.

---
Created/updated by project maintainer.