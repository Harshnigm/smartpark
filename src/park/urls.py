
from django.conf.urls import url,include
from django.contrib import admin

from .views import(
	   park_home,
	   park_create,
	   park_list,
	   graphs,
           post_create,
           user_list

	)

urlpatterns = [
    url(r'^$', park_home),
    url(r'^create/(?P<id>\d+)/$', park_create),
    url(r'^list/$', park_list),
    url(r'^graph/$', graphs),
    url(r'^form/$',post_create),
    url(r'^user/$',user_list)

    #url(r'^create/$', "park.views.park_home"),
]
