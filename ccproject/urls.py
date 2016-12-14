"""ccproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

# all apps urls import
from accounts import urls as accounts_urls
from frontend import urls as frontend_urls
from payment import urls as payment_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(frontend_urls, namespace='frontend')),
    url(r'^accounts/', include(accounts_urls, namespace='accounts')),
    url(r'^payment/', include(payment_urls, namespace='payment'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
