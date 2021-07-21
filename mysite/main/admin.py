from django.contrib import admin
from .models import Articles, Projects, Courses, Product

# Register your models here.
admin.site.register(Articles)
admin.site.register(Projects)
admin.site.register(Courses)
admin.site.register(Product)
