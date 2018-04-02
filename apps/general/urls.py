from django.conf.urls import url,include
from django.contrib import admin

from apps.general.views import conocenos_index_view

urlpatterns = [
    url(r'^$', conocenos_index_view, name = 'conocenosIndex')
]