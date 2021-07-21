from main.models import Articles
from django.shortcuts import render
from .medium_scraper import add_new_article
from django.views.generic import ListView
#from .articles import change_all_tags, add_all_articles
# Create your views here.


class Homepage(ListView):
    model = Articles
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        article_data = super(Homepage, self).get_context_data(**kwargs)
        article_data['left'] = Articles.objects.order_by('-date_created')[
            :2]
        article_data['right'] = Articles.objects.order_by('-date_created')[
            2:4]
        return article_data

    '''
    def get_queryset(self, *args, **kwargs):
        qs = super(Homepage, self).get_queryset(*args, **kwargs)
        qs['left-col'] = qs.order_by("-date_created")[:2]
        qs['right-col'] = qs.order_by("-date_created")[2:4]
        return qs
    '''


'''
def homepage(request):
    latest_articles = Articles.objects.order_by('-date_created')[:4]
    return render(request, template_name=, context={articles: latest_articles})
'''


class ArticlePage(ListView):
    template_name = "main/articles.html"
    model = Articles


def courses(request):
    return render(request, template_name="main/courses.html")


def resources(request):
    return render(request, template_name="main/resources.html")


def projects(request):
    return render(request, template_name="main/projects.html")


def about(request):
    return render(request, template_name="main/about.html")
