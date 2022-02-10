from django.contrib import admin
from .models import MovieDetail, MovieLink, MovieStars, Genres, PloteKewords, MovieActor, InTheater, CastCrew\
    , Reviews, User
# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ['pic']


@admin.register(MovieStars)
class MovieStarsAdmin(admin.ModelAdmin):
    fields = ['stars_name', 'stars_gender', 'stars_age']


@admin.register(Genres)
class GenresAdmin(admin.ModelAdmin):
    fields = ['movie_type']


@admin.register(PloteKewords)
class PloteKeywordsAdmin(admin.ModelAdmin):
    fields = ['plote_keywords']


@admin.register(MovieDetail)
class MovieDetailAdmin(admin.ModelAdmin):
    fields = ['is_slider', 'image', 'title', 'type', 'rating', 'writter', 'director', 'description', 'release_date', 'run_time', 'mmpa_rating', 'plote_words']


@admin.register(MovieLink)
class MovieLinkAdmin(admin.ModelAdmin):
    fields = ['link']


@admin.register(MovieActor)
class MovieActorAdmin(admin.ModelAdmin):
    fields = ['actor_type', 'actor_title', 'actor_images']


@admin.register(InTheater)
class InTheaterAdmin(admin.ModelAdmin):
    fields = ['theater_images', 'theater_desc', 'theater_duration']


@admin.register(CastCrew)
class CastCrewAdmin(admin.ModelAdmin):
    fields = ['cast_image', 'cast_title', 'cast_type']


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    fields = ['user_pic', 'movie_details', 'name', 'comment', 'date', 'title', 'rate']