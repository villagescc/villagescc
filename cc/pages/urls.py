from django.conf.urls import patterns, url
from django.views.generic import TemplateView, RedirectView

urlpatterns = patterns(
    'cc.pages.views',
    url(r'^$', 'intro', name='home'),
    url(r'^feedback/$', 'feedback', name='feedback'),
    url(r'^about/$', RedirectView.as_view(url='/about/motivation/'), name='about'),
    url(r'^about/how/$', TemplateView.as_view(template_name='how_it_works.html'), name='how_it_works'),
    url(r'^about/privacy/$', TemplateView.as_view(template_name='privacy.html'), name='privacy'),
    url(r'^about/motivation/$', TemplateView.as_view(template_name='motivation.html'), name='motivation'),
    url(r'^about/developers/$', TemplateView.as_view(template_name='developers.html'), name='developers'),
    url(r'^about/donate/$', TemplateView.as_view(template_name='donate.html'), name='donate'),
)
