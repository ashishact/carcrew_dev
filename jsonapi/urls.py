from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^cars/$', views.car_list),
    url(r'^cars/(?P<pk>[0-9]+)/$', views.car_detail),

    url(r'^products/$', views.product_list),
    url(r'^products/(?P<pk>[0-9]+)/$', views.product_detail),

    url(r'^garages/$', views.garage_list),
    url(r'^garages/(?P<pk>[0-9]+)/$', views.garage_detail),

    url(r'^$', views.index, name='index'),
]