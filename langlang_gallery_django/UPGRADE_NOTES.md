# Upgrade Notes (v2)

This version adds:
1) Gallery image uploads via Django Admin (GalleryImage model)
2) Rich text editor for Section.body (django-ckeditor)

## Install / upgrade
```bash
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Upload images
Admin → Site Content → Sections → open **gallery** → add **Gallery Images** inline

## Rich text
Admin → Site Content → Sections → edit the Body field using CKEditor.
