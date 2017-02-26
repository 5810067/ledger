from django.conf.urls import url

from . import views

app_name = 'ledger'
urlpatterns =[
    url(r'^$', views.index, name='index'),
    url(r'download/', views.download,name='download'),
    url(r'^add_list/$', views.add_list, name='add_list'),
    url(r'^edit_list/$', views.edit_list, name='edit_list'),
    url(r'^del_list/(?P<note_id>[0-9]+)/$', views.del_list, name='del_list'),
    url(r'^verify/$', views.verify, name='verify'),
    url(r'^theme_page/$', views.theme_select, name='theme_select'),
    url(r'^change_theme/$', views.change_theme, name='change_theme'),   
]