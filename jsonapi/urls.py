from django.conf.urls import url
from django.views.generic import TemplateView
from rest_framework.urlpatterns import format_suffix_patterns

from . import api, views

urlpatterns = [
    url(r'^cars/$', api.CarList.as_view()),
    url(r'^cars/(?P<pk>[0-9]+)/$', api.CarDetail.as_view()),

    url(r'^products/$', api.ProductList.as_view()),
    url(r'^products/(?P<pk>[0-9]+)/$', api.ProductDetail.as_view()),

    url(r'^garages/$', api.GarageList.as_view()),
    url(r'^garages/(?P<pk>[0-9]+)/$', api.GarageDetail.as_view()),

    url(r'^manufacturers/$', api.ManufacturerList.as_view()),
    url(r'^manufacturers/(?P<pk>[0-9]+)/$', api.ManufacturerDetail.as_view()),

    url(r'^address/$', api.AddressList.as_view()),
    url(r'^address/(?P<pk>[0-9]+)/$', api.AddressDetail.as_view()),

    url(r'^category/$', api.CategoryList.as_view()),
    url(r'^category/(?P<pk>[0-9]+)/$', api.CategoryDetail.as_view()),

    url(r'^category_description/$', api.CategoryDescriptionList.as_view()),
    url(r'^category_description/(?P<pk>[0-9]+)/$', api.CategoryDescriptionDetail.as_view()),

    url(r'^$', views.index, name='index'),
    url(r'^index/$', TemplateView.as_view(template_name='index.html'), name="home"),
]

urlpatterns = format_suffix_patterns(urlpatterns)