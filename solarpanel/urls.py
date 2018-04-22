from django.conf.urls import url

from . import views

app_name = 'solarpanel'

urlpatterns = [

url(r'^$',views.IndexView.as_view(),name='index'),

# list view

url(r'^list/$',views.ContentListView.as_view(),name='list'),

url(r'^banner/detail/(?P<pk>\d+)$',views.ContentDetailView.as_view(),name='contentdetail'),

url(r'^banner/$',views.BannerDetailView.as_view(),name='Banner'),
url(r'^banner/update/(?P<pk>\d+)$',views.BannerUpdateView.as_view(),name='bannerupdate'),
url(r'^banner/delete/(?P<pk>\d+)$',views.BannerDeleteView.as_view(),name='bannerdelete'),

url(r'^projects/$',views.ProjectDetailView.as_view(),name='Project'),
url(r'^projects/update/(?P<pk>\d+)$',views.ProjectsUpdateView.as_view(),name='projectupdate'),
url(r'^projects/delete/(?P<pk>\d+)$',views.ProjectsDeleteView.as_view(),name='projectdelete'),

url(r'^career/$',views.CareerDetailView.as_view(),name='Career'),
url(r'^career/update/(?P<pk>\d+)$',views.CareerUpdateView.as_view(),name='careerupdate'),
url(r'^career/delete/(?P<pk>\d+)$',views.CareerDeleteView.as_view(),name='careerdelete'),

url(r'^team/$',views.TeamDetailView.as_view(),name='Team'),
url(r'^team/update/(?P<pk>\d+)$',views.TeamUpdateView.as_view(),name='teamupdate'),
url(r'^team/delete/(?P<pk>\d+)$',views.TeamDeleteView.as_view(),name='teamdelete'),

url(r'^media/$',views.MediaDetailView.as_view(),name='Media'),
url(r'^media/update/(?P<pk>\d+)$',views.MediaUpdateView.as_view(),name='mediaupdate'),
url(r'^media/delete/(?P<pk>\d+)$',views.MediaDeleteView.as_view(),name='mediadelete'),

]
