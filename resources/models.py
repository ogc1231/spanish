from django.db import models
from django.contrib.auth.models import User


class Resource(models.Model):

    image_filter_choices = [
        ('_1977', '1977'),
        ('brannan', 'Brannan'),
        ('earlybird', 'Earlybird'),
        ('hudson', 'Hudson'),
        ('inkwell', 'Inkwell'),
        ('lofi', 'Lo-Fi'),
        ('kelvin', 'Kelvin'),
        ('normal', 'Normal'),
        ('nashville', 'Nashville'),
        ('rise', 'Rise'),
        ('toaster', 'Toaster'),
        ('valencia', 'Valencia'),
        ('walden', 'Walden'),
        ('xpro2', 'X-pro II')
    ]

    country_filter_choices = [
        ('mixed', 'Mixed'),
        ('argentina', 'Argentina'),
        ('bolivia', 'Bolivia'),
        ('canary_islands', 'Canary Islands'),
        ('chile', 'Chile'),
        ('colombia', 'Colombia'),
        ('costa_rica', 'Costa Rica'),
        ('cuba', 'Cuba'),
        ('dominican_republic', 'Dominican Republic'),
        ('ecuador', 'Ecuador'),
        ('el_salvador', 'El Salvador'),
        ('equatorial_guinea', 'Equatorial Guinea'),
        ('guatemala', 'Guatemala'),
        ('honduras', 'Honduras'),
        ('mexico', 'Mexico'),
        ('nicaragua', 'Nicaragua'),
        ('panama', 'Panama'),
        ('paraguay', 'Paraguay'),
        ('peru', 'Peru'),
        ('spain', 'Spain'),
        ('uruguay', 'Uruguay'),
        ('venezuela', 'Venezuela'),
    ]

    resource_type_filter_choices = [
        ('podcast_listen', 'Podcast/Listening'),
        ('youtube_video', 'YouTube/Video'),
        ('book_read', 'Book/Reading'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_post_ve6bmd', blank=True
    )
    image_filter = models.CharField(
        max_length=32, choices=image_filter_choices, default='normal'
    )
    link = models.URLField(max_length=100, unique=True)
    country_filter = models.CharField(
        max_length=32, choices=country_filter_choices, default='normal'
    )
    resource_type_filter = models.CharField(
        max_length=32, choices=resource_type_filter_choices, default='normal'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'