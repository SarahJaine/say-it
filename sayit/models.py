from django.db import models


class Example(models.Model):
    title = models.CharField(max_length=80)
    product_type = models.CharField(max_length=100)
    review = models.TextField(max_length=500, unique=True)
    media_link = models.URLField(blank=True, null=True, max_length=100)
    audio_image = models.ImageField(blank=True, null=True, upload_to='examples/')
    media = models.FileField(blank=True, null=True, upload_to='examples/')
    order = models.IntegerField(default=0)
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
    )
    status = models.CharField(max_length=1, choices=STATUS_CHOICES,
                              default='d')

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title


class Musician(models.Model):
    name = models.CharField(max_length=80, unique=True)
    position = models.CharField(max_length=100)
    musical_styles = models.CharField(max_length=100)
    image = models.ImageField(blank=True, null=True, upload_to='musicians/')
    bio = models.TextField(max_length=500, unique=True)
    profile_url = models.URLField(blank=True, null=True, max_length=100)
    song_url_1 = models.URLField(blank=True, null=True, max_length=100)
    song_name_1 = models.CharField(blank=True, null=True, max_length=80)
    song_url_2 = models.URLField(blank=True, null=True, max_length=100)
    song_name_2 = models.CharField(blank=True, null=True, max_length=80)
    order = models.IntegerField(default=0)
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
    )
    status = models.CharField(max_length=1, choices=STATUS_CHOICES,
                              default='d')

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.name
