"""oozaaoo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls.static import static,serve
from django.conf import settings
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
	# url(r'^jet/', include('jet.urls', 'jet')),
	# url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    url(r'^admin/', admin.site.urls),
    url(r'^', admin.site.urls),
    url(r'^total_amount_generation/$', csrf_exempt(views.total_amount_generation)),
    # url(r'^total_amount_generation/$', 'master.views.total_amount_generation','total_amount_generation'),
    # url(r'^total_amount_generation/', include('master.urls', 'total_amount_generation')),
]
if settings.DEBUG:
    urlpatterns += [
        url(r'^(?P<path>.*)/$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
    urlpatterns += [
        url(r'^static/(?P<path>.*)/$', serve, {
            'document_root': settings.STATIC_ROOT,
        }),
    ]
