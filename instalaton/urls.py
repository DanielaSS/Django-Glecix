from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.instalaton_list, name='instalaton_list'),
]