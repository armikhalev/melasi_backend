from django.conf.urls import url
from . import views

urlpatterns = [
		url('^english/(?P<letter>.+)/$', views.WordSet.as_view()),
		url('^mela/(?P<letter>.+)/$', views.LaSet.as_view()),
]
