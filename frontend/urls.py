from django.conf.urls import url
# frontend views import
from frontend import views


urlpatterns = [
    url(r'^$', views.home),
    url(r'^post-login$', views.post_login_home),
    url(r'^profile$', views.profile),
]
