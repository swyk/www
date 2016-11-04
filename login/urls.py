from django.conf.urls import include, url

import login.views as views

urlpatterns = [
    url(r'^$',views.home),
    url(r'^login$',views.login),
]
