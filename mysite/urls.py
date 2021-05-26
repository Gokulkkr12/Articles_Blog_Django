

from django.contrib import admin
from django.conf.urls import url,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    url(r'^$',views.homepage),
    url(r'^about/$',views.about),
    url(r'^accounts/',include('accounts.urls')),
    url(r'^articles/',include('articles.urls')),
    url(r'^admin/',admin.site.urls),





]

urlpatterns+=staticfiles_urlpatterns()