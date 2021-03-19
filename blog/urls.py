
from django.urls import path, re_path


from . import views


app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    re_path('^posts/(?P<id>[0-9]+)$', views.show, name='show'),
]
