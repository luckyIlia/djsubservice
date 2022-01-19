from django.db import models


class Course(model.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    thumbnail = models.ImageField(upload_to="thumbnails/")

    def __str__(self):
        return self.name

class Video(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='videos')
    vimeo_id = models.CharField(max_length=50)
    title = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.title

