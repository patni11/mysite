from django.db import models

# Create your models here.


class Articles(models.Model):
    title = models.CharField(max_length=300)
    date_created = models.DateField()
    medium_link = models.URLField(
        default="Blog is not available for this project")
    image = models.ImageField(
        upload_to="article_images/", blank=True, null=True)
    tags = models.CharField(max_length=255, default="No Tag")

    def __str__(self):
        return self.title


class Projects(models.Model):
    title = models.CharField(max_length=300)
    sub_heading = models.TextField()
    # image
    description = models.TextField()
    youTube_video_link = models.URLField(
        default="Video is not available for this project")
    medium_link = models.URLField(
        default="Blog is not available for this project")
    tech_used = models.CharField(max_length=300)
    gitHub_link = models.URLField(default="Project is not available on Github")

    def __str__(self):
        return self.title


class Courses(models.Model):
    title = models.CharField(max_length=300)
    image = models.ImageField(
        upload_to="courses/", blank=True, null=True)
    course_link = models.URLField(default="Course is not currently available")
    cost = models.CharField(max_length=10, default="Free")

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=300)
    image = models.ImageField(upload_to="", blank=True)
    product_link = models.URLField(
        default="Product is not available")

    def __str__(self):
        return self.title


class About(models.Model):
    header = models.TextField()
    now = models.TextField()
    learning = models.TextField()
    get_in_touch = models.TextField()

    def __str__(self):
        return "about"
