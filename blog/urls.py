from .views import BlogListView
from django.urls import path

urlpatterns = [
    path("" , BlogListView , name="blog_list_view"),
]