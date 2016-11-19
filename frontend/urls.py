from django.conf.urls import url
# frontend views import
from frontend import views


urlpatterns = [
    url(r'^$', views.home),
]
