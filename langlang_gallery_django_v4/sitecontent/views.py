
from django.views.generic import TemplateView
from .models import Section,SiteSettings
class HomePageView(TemplateView):
    template_name="home.html"
    def get_context_data(self,**kwargs):
        ctx=super().get_context_data(**kwargs)
        ctx["settings"]=SiteSettings.objects.first() or SiteSettings.objects.create()
        secs=Section.objects.filter(is_active=True)
        ctx["sections"]=secs
        ctx["sections_by_slug"]={s.slug:s for s in secs}
        return ctx
