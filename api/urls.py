from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^productapi/$', views.product_list),
    url(r'^productapi/(?P<pk>[0-9]+)/$', views.product_detail),
    url(r'^$', views.index, name='index'),
]