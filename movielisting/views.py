from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse

from movielisting.models import Movie

def index(request):
    all_movies = Movie.objects.order_by('movie_title')
    context = {'all_movies' : all_movies}
    return render(request,'movies/index.html',context)

def detail(request, movie_title):
    movie = get_object_or_404(Movie, movie_title=movie_title)
    context = {'movie' : movie}
    return render(request,'movies/details.html',context)


def search(request):
	if request.method == 'POST':
		query = request.POST["search"]
		posts = Post.objects.filter(movie_title__icontains=query)
		jsonDec = json.decoder.JSONDecoder()
