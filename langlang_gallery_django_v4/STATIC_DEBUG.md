
# Static debug checklist

If the page looks unstyled, check these in your browser:

1) Open http://127.0.0.1:8000/static/css/styles.css
   - You should see CSS text (not 404).

2) In settings.py you should have:
   STATIC_URL = '/static/'
   STATICFILES_DIRS = [BASE_DIR / 'static']

3) In home.html:
   {% load static %}
   <link rel="stylesheet" href="{% static 'css/styles.css' %}">
