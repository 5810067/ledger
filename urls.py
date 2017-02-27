from django.conf.urls import url
from . import views

app_name = 'ledger'
urlpatterns =[
    url(r'^(?P<theme>[a-zA-Z0-9]+)/$', views.index, name='index'),
    url(r'^download/$', views.download,name='download'),
    url(r'^add_list/(?P<theme>[a-zA-Z0-9]+)/$', views.add_list, name='add_list'),
    url(r'^edit_list/(?P<theme>[a-zA-Z0-9]+)/$', views.edit_list, name='edit_list'),
    url(r'^del_list/(?P<theme>[a-zA-Z0-9]+)/(?P<note_id>[0-9]+)/$', views.del_list, name='del_list'),
    url(r'^verify/(?P<theme>[a-zA-Z0-9]+)/$', views.verify, name='verify'),
    url(r'^theme_page/(?P<theme>[a-zA-Z0-9]+)/$', views.theme_select, name='theme_page'),
    url(r'^change_theme/$', views.change_theme, name='change_theme'),   
]