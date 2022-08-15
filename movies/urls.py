from django.urls import path
from .views import homepage
from .views import(
    MovieListView, 
    MovieDetailView,
    MovieCreateView,
    MovieUpdateView,
    MovieDeleteView
    ) 


urlpatterns = [

	path('', MovieListView.as_view(), name='home'),
	path('movie/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
    path('movie/new/', MovieCreateView.as_view(), name='movie-create'),
    path('movie/<int:pk>/update/', MovieUpdateView.as_view(), name='movie-update'),
    path('movie/<int:pk>/delete/', MovieDeleteView.as_view(), name='movie-delete'),
]