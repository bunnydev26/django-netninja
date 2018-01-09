from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = "article"

urlpatterns = [
    url(r'^$', views.article_list, name="list"),
    url(r'^(?P<slug>[\w\-]+)/$', views.article_details, name="detail"),
]

urlpatterns += staticfiles_urlpatterns()
