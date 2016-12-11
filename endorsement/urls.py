from django.conf.urls import url
# frontend views import
from endorsement import views


urlpatterns = [
    url(r'^endorsement/$', views.endorsement, name='endorsement'),
]
