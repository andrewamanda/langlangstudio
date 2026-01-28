
from django.contrib import admin
from .models import Section,SiteSettings,GalleryImage

class GalleryInline(admin.TabularInline):
    model=GalleryImage
    fields=("order","image","thumb","title","caption","is_active")
    readonly_fields=("thumb",)
    extra=1

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display=("slug","order","title","is_active")
    list_editable=("order","is_active")
    list_display_links=("slug",)
    def get_inlines(self,request,obj=None):
        if obj and obj.slug=="gallery":
            return [GalleryInline]
        return []

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    pass
