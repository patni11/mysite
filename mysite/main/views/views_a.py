from main.models import Articles, Courses, Product
from django.shortcuts import render
from .medium_scraper import add_new_article
from django.views.generic import ListView
from .articles import left_middle_right
from .courses import left_right
# Create your views here.


class Homepage(ListView):
    model = Articles
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        article_data = super(Homepage, self).get_context_data(**kwargs)
        articles = Articles.objects.order_by('-date_created')

        article_data['left'] = articles[:2]
        article_data['right'] = articles[2:4]
        return article_data


class ArticlePage(ListView):
    model = Articles
    template_name = "main/articles.html"

    def get_context_data(self, **kwargs):
        article_data = super(ArticlePage, self).get_context_data(**kwargs)

        tag = self.kwargs.get('tag', None)
        if tag != None:
            if tag in "Tech Programming Productivity Crypto":
                articles = Articles.objects.filter(
                    tags=tag).order_by('-date_created')
        else:
            articles = Articles.objects.order_by('-date_created')

        left, middle, right = left_middle_right(articles)
        article_data['left'] = left
        article_data['middle'] = middle
        article_data['right'] = right
        return article_data


class CoursePage(ListView):
    model = Courses
    template_name = "main/courses.html"

    def get_context_data(self, **kwargs):
        course_data = super(CoursePage, self).get_context_data(**kwargs)
        courses = Courses.objects.all()
        left, right = left_right(courses)

        course_data['left'] = left
        course_data['right'] = right

        return course_data


class ResourcesPage(ListView):
    model = Product
    template_name = "main/resources.html"

    def get_context_data(self, **kwargs):
        resource_data = super(ResourcesPage, self).get_context_data(**kwargs)
        resources = Product.objects.all()
        left, right = left_right(resources)

        resource_data['left'] = left
        resource_data['right'] = right

        return resource_data


def projects(request):
    return render(request, template_name="main/projects.html")


def about(request):
    return render(request, template_name="main/about.html")
