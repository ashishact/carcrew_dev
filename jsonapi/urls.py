from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^cars/$', views.car_list),
    url(r'^cars/(?P<pk>[0-9]+)/$', views.car_detail),

    url(r'^products/$', views.product_list),
    url(r'^products/(?P<pk>[0-9]+)/$', views.product_detail),

    url(r'^garages/$', views.garage_list),
    url(r'^garages/(?P<pk>[0-9]+)/$', views.garage_detail),

    url(r'^$', views.index, name='index'),
    url(r'^index/$', TemplateView.as_view(template_name='index.html'), name="home"),
]
