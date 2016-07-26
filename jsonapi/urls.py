from django.conf.urls import url
from django.views.generic import TemplateView
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    url(r'^cars/$', views.CarList.as_view()),
    url(r'^cars/(?P<pk>[0-9]+)/$', views.CarDetail.as_view()),

    url(r'^products/$', views.ProductList.as_view()),
    url(r'^products/(?P<pk>[0-9]+)/$', views.ProductDetail.as_view()),

    url(r'^garages/$', views.GarageList.as_view()),
    url(r'^garages/(?P<pk>[0-9]+)/$', views.GarageDetail.as_view()),

    url(r'^$', views.index, name='index'),
    url(r'^index/$', TemplateView.as_view(template_name='index.html'), name="home"),
]

urlpatterns = format_suffix_patterns(urlpatterns)