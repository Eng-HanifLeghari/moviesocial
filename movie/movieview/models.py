from django.db import models
from django.contrib.auth.models import User


class User(User):
    pic = models.ImageField(upload_to="{% static 'images/", null=True, blank=True, default='plceholder.png')


class MovieStars(models.Model):
    stars_name = models.CharField(max_length=300, null=True, blank=True)
    stars_gender = models.CharField(max_length=300, null=True, blank=True)
    stars_age = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.stars_name


class Genres(models.Model):
    movie_type = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.movie_type


class PloteKewords(models.Model):
    plote_keywords = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.plote_keywords


class MovieDetail(models.Model):
    is_slider = models.BooleanField(default=False)
    image = models.ImageField(upload_to="{% static 'images/", null=True, blank=True, default='plceholder.png')
    title = models.CharField(max_length=300, null=True, blank=True)
    type = models.CharField(max_length=300, null=True, blank=True)
    rating = models.FloatField(null=True, blank=True)
    writter = models.CharField(max_length=400, null=True, blank=True)
    director = models.CharField(max_length=300, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    release_date = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    stars = models.ManyToManyField(MovieStars, null=True, blank=True)
    genres = models.ManyToManyField(Genres, null=True, blank=True)
    run_time = models.CharField(max_length=250, null=True, blank=True)
    mmpa_rating = models.CharField(max_length=250, null=True, blank=True)
    plote_words = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.title)


class MovieLink(models.Model):
    link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.link


class InTheater(models.Model):
    theater_images = models.ImageField(upload_to="{% static 'images/", null=True, blank=True, default='plceholder.png')
    theater_desc = models.CharField(max_length=300, null=True, blank=True)
    theater_duration = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.theater_desc


class MovieActor(models.Model):
    actor_type = models.CharField(max_length=300, null=True, blank=True)
    actor_title = models.CharField(max_length=300, null=True, blank=True)
    actor_images = models.ImageField(upload_to="{% static 'images/", null=True, blank=True, default='plceholder.png')

    def __str__(self):
        return self.actor_type


class CastCrew(models.Model):
    cast_image = models.ImageField(upload_to="{% static 'images/", null=True, blank=True, default='plceholder.png')
    cast_title = models.CharField(max_length=300, null=True, blank=True)
    cast_type = models.CharField(max_length=240, null=True, blank=True)

    def __str__(self):
        return self.cast_title


class Reviews(models.Model):
    user_pic = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='user_movie')
    movie_details = models.ForeignKey(MovieDetail, on_delete=models.CASCADE, blank=True, null=True, related_name='movie_detail')
    name = models.CharField(max_length=30)
    comment = models.TextField(max_length=250)
    title = models.CharField(max_length=300)
    rate = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)

    def get_rate(self):
        return self.name