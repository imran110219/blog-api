from django.conf.urls import url
from django.contrib import admin
from .views import(
    post_category,
    post_list,
    category_post_list,
    post_create,
    post_detail,
    post_update,
    post_delete,
)

urlpatterns = [

    url(r'^category/$', post_category, name="category"),
    url(r'^$', post_list, name="list"),
    url(r'^$', category_post_list, name="category_list"),
    url(r'^create/$', post_create),
    url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', post_update, name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', post_delete),
]