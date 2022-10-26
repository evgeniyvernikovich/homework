"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hello_world.views import hello_world
from reference_books import views as ref_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello-world/', hello_world),
    path('show-authors-list/<int:pk>/', ref_views.ShowAuthors.as_view()),
    path('show-author-create/', ref_views.CreateAuthor.as_view()),
    path('show-author-update/<int:pk>/', ref_views.UpdateAuthor.as_view()),
    path('show-author-delete/<int:pk>/', ref_views.DeleteAuthor.as_view()),
    path('show-author-detail/<int:pk>/', ref_views.ShowAuthor.as_view()),
    path('show-serie-create/', ref_views.CreateSerie.as_view()),
    path('show-serie-update/<int:pk>/', ref_views.UpdateSerie.as_view()),
    path('show-serie-delete/<int:pk>/', ref_views.DeleteSerie.as_view()),
    path('show-serie-detail/<int:pk>/', ref_views.ShowSerie.as_view()),
    path('show-serie-list/<int:pk>/', ref_views.ShowSerie.as_view()),
    path('show-serie-create/', ref_views.CreateGenre.as_view()),
    path('show-genre-update/<int:pk>/', ref_views.UpdateGenre.as_view()),
    path('show-genre-delete/<int:pk>/', ref_views.DeleteGenre.as_view()),
    path('show-genre-detail/<int:pk>/', ref_views.ShowGenre.as_view()),
    path('show-genres-list/<int:pk>/', ref_views.ShowGenres.as_view()),
        path('show-publishing-create/', ref_views.CreatePublishing.as_view()),
    path('show-publishing-update/<int:pk>/', ref_views.UpdatePublishing.as_view()),
    path('show-publishing-delete/<int:pk>/', ref_views.DeletePublishing.as_view()),
    path('show-publishing-detail/<int:pk>/', ref_views.ShowPublishing.as_view()),
    path('show-publishings-list/<int:pk>/', ref_views.ShowPublishings.as_view()),



]
