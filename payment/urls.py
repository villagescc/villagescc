from django.conf.urls import url
# frontend views import
from payment import views


urlpatterns = [
    url(r'^payment$', views.payment, name='payment'),
]
