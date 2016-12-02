from django.conf.urls import url
# frontend views import
from frontend import views


urlpatterns = [
    url(r'^$', views.home),
    url(r'^post-login/$', views.post_login),
    url(r'^profile/$', views.profile),
    url(r'^payment/$', views.payment),
    url(r'^endorsement/$', views.endorsement),
]
