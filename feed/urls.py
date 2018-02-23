"""instame URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from .views import (
	FeedDetailView,
	FeedDeleteView,
	FeedListView,
	FeedCreateView,
	FeedUpdateView,
	

	)

urlpatterns = [
	url(r'^$',FeedListView.as_view(), name='list'),
	url(r'^create/$',FeedCreateView.as_view(), name='create'),    
    url(r'^(?P<pk>\d+)/update/$',FeedUpdateView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/$',FeedDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/delete/$',FeedDeleteView.as_view(), name='delete')
]

 