# Django version of the flat HTML page

This project makes the text on each page section editable via Django Admin.

## Quick start
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Admin:
- http://127.0.0.1:8000/admin/

Edit content:
- Admin → Site Content → Sections
- Admin → Site Content → Site Settings

## Gallery images
Put your images under `static/images/` following the same folder/filenames referenced in `templates/home.html`.
