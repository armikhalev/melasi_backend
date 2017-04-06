from django.conf.urls import url
from . import views

urlpatterns = [
	    url('^a-words/$', views.A_WordSet.as_view()),
	    url('^d-words/$', views.D_WordSet.as_view()),
	    url('^f-words/$', views.F_WordSet.as_view()),
	    url('^a-las/$', views.A_LaSet.as_view()),
	    url('^d-las/$', views.D_LaSet.as_view()),
	    url('^f-las/$', views.F_LaSet.as_view()),
]
