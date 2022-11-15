from django.urls import path
from . import views
app_name = 'reference_books'

urlpatterns = [
    path('show-authors-list/', views.ShowAuthors.as_view(), name='sh-aut-list'),
    path('show-author-create/', views.CreateAuthor.as_view(), name='sh-aut-create'),
    path('show-author-update/<int:pk>/', views.UpdateAuthor.as_view(), name='sh-aut-update'),
    path('show-author-delete/<int:pk>/', views.DeleteAuthor.as_view(), name='sh-aut-delete'),
    path('show-author-detail/<int:pk>/', views.ShowAuthor.as_view(), name='sh-aut-detail'),
    path('show-serie-create/', views.CreateSerie.as_view(), name='sh-ser-create'),
    path('show-serie-update/<int:pk>/', views.UpdateSerie.as_view(), name='sh-ser-update'),
    path('show-serie-delete/<int:pk>/', views.DeleteSerie.as_view(), name='sh-ser-delete'),
    path('show-serie-detail/<int:pk>/', views.ShowSerie.as_view(), name='sh-ser-detail'),
    path('show-series-list/', views.ShowSeries.as_view(), name='sh-ser-list'),
    path('show-genre-create/', views.CreateGenre.as_view(), name='sh-gen-create'),
    path('show-genre-update/<int:pk>/', views.UpdateGenre.as_view(), name='sh-gen-update'),
    path('show-genre-delete/<int:pk>/', views.DeleteGenre.as_view(), name='sh-gen-delete'),
    path('show-genre-detail/<int:pk>/', views.ShowGenre.as_view(), name='sh-gen-detail'),
    path('show-genres-list/', views.ShowGenres.as_view(), name='sh-gen-list'),
    path('show-publishing-create/', views.CreatePublishing.as_view(), name='sh-pub-create'),
    path('show-publishing-update/<int:pk>/', views.UpdatePublishing.as_view(), name='sh-pub-update'),
    path('show-publishing-delete/<int:pk>/', views.DeletePublishing.as_view(), name='sh-pub-delete'),
    path('show-publishing-detail/<int:pk>/', views.ShowPublishing.as_view(), name='sh-pub-detail'),
    path('show-publishings-list/', views.ShowPublishings.as_view(), name='sh-pub-list'),
]