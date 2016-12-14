from django.conf.urls import url

# Import Accounts views
from accounts import views


urlpatterns = [
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^settings/$', views.settings_view, name='settings'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^signup/$', views.signup_view, name='signup'),
    url(r'^logout/$', views.logout_view, name='logout')
]
