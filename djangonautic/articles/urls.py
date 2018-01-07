from django.conf.urls import url
from . import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^$', views.article_list),
]

urlpatterns += staticfiles_urlpatterns()
