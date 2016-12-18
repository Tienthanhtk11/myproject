"""Project5_Izischool URL Configuration

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
from django.contrib import admin

from course import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^course/$',views.ListCourseView.as_view()),
    url(r'^course/detail/([0-9]+)/$',views.DetailCourseView.as_view()),
    url(r'^course/new/$',views.PostCourseView.as_view()),
    url(r'^course/edit/([0-9]+)/$',views.EditCourseView.as_view()),
    url(r'^course/delete/([0-9]+)/$',views.DeleteCourseView.as_view()),
    url(r'^course/searchResult/name?=([A-Z])/$',views.SearchCourse.as_view()),
]
