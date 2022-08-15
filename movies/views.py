from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Movies
from django.shortcuts import get_object_or_404
from django.views.generic import(
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
    )


def homepage(request):
	movies = Movies.objects.all()
	return render(request, 'index.html', {'movies': movies})

# movie list class
class MovieListView(ListView):
    model = Movies
    template_name = 'index.html'
    context_object_name = 'movies'
    ordering = ['-released_date']
    paginate_by = 4

# movie datail class
class MovieDetailView(DetailView):
    model = Movies
    template_name = 'movie_details.html'

 
class MovieCreateView(LoginRequiredMixin, CreateView):
    model = Movies
    fields = ['title', 'released_date', 'length_time', 'description', 'trail_link', 'movies_image']
    template_name = 'movie_form.html'

    def form_valid(self, form):
        form.instance.manager = self.request.user
        return super().form_valid(form)


class MovieUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Movies
    fields = ['title', 'released_date', 'length_time', 'description', 'trail_link', 'movies_image']
    template_name = 'movie_form.html'

    def form_valid(self, form):
        form.instance.manager = self.request.user
        return super().form_valid(form)

    def test_func(self):
        movie = self.get_object()
        if self.request.user == movie.manager:
            return True
        return False

class MovieDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Movies
    template_name = 'movie_confirm_delete.html'
    success_url = '/'



    def test_func(self):
        post = self.get_object()
        if self.request.user == post.manager:
            return True
        return False