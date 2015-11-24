from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index$', views.index, name='index'),
    url(r'^results$', views.results, name='results'),
    url(r'^text/', 'polls.views.text'),
    url(r'^u_rl/', 'polls.views.u_rl'),
]
