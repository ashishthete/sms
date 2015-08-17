from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
	url(r'^(?P<person_id>[0-9]+)/print$', views.printBill, name='print'),
	url(r'^(?P<bill_id>[0-9]+)/pdf_view*', views.myview, name='pdf_view'),
]
