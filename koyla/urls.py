from django.conf.urls import url
from . import views

urlpatterns = [
		url('^words/$', views.WordSet.as_view()),
		url('^las/$', views.LaSet.as_view()),
		url('^cards/$', views.CardSet.as_view()),
]
