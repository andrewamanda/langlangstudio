from django.db import migrations

HOME_TEXT = """Welcome to the creative world of Langlang, a remarkably talented 9th-grade visual artist with a passion for painting. As you explore this website, you'll be immersed in the extraordinary talent and vision of a young artist on a journey to transform her passion into a thriving career. Langlang's artwork reflects the depth of her imagination and the boundless possibilities of artistic expression. From evocative landscapes to captivating portraits, each piece showcases her unique ability to capture emotion and convey meaningful narratives. We invite you to join Langlang on her artistic adventure, as she continues to nurture her talent and share her love for visual art with the world. Let the beauty of her work inspire you and evoke a sense of wonder, as we celebrate the creative spirit of this budding artist. Welcome, and enjoy your visit!"""

ABOUT_TEXT = """Langlang is a gifted young painter currently in the 9th grade, with a passion for visual art that transcends her years. Possessing a remarkable talent, she has dedicated herself to exploring the vast world of artistic expression and refining her own unique style. Langlang's journey in the visual arts has been filled with vibrant colors, bold textures, and deeply emotional narratives, which she masterfully weaves into every piece she creates. Inspired by both the beauty of nature and the intricacies of the human experience, her artwork reflects a genuine understanding of the world around her. As Langlang pursues a career in the visual arts, her unwavering dedication and love for her craft will undoubtedly lead her to new heights, forging a path that is as vivid and unforgettable as her artwork."""

CONTACT_TEXT = """If you're interested in purchasing any artwork or have any questions, please feel free to contact us."""

def seed(apps, schema_editor):
    SiteSettings = apps.get_model("sitecontent", "SiteSettings")
    Section = apps.get_model("sitecontent", "Section")

    # Site title + footer (match original)
    SiteSettings.objects.update_or_create(
        id=1,
        defaults={
            "site_title": "Langlang's Art Gallery",
            "footer_text": "© 2023 My Daughter's Art Gallery. All rights reserved.",
        },
    )

    # Sections (match original structure)
    sections = [
        dict(slug="home",    nav_label="Home",    title="Welcome!", body=HOME_TEXT,    order=10, is_active=True),
        dict(slug="gallery", nav_label="Gallery", title="Gallery",  body="",          order=20, is_active=True),
        dict(slug="about",   nav_label="About",   title="About",    body=ABOUT_TEXT,  order=30, is_active=True),
        dict(slug="contact", nav_label="Contact", title="Contact",  body=CONTACT_TEXT,order=40, is_active=True),
    ]

    for s in sections:
        Section.objects.update_or_create(slug=s["slug"], defaults=s)

def unseed(apps, schema_editor):
    SiteSettings = apps.get_model("sitecontent", "SiteSettings")
    Section = apps.get_model("sitecontent", "Section")
    Section.objects.all().delete()
    SiteSettings.objects.all().delete()

class Migration(migrations.Migration):
    dependencies = [
        ("sitecontent", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed, unseed),
    ]

