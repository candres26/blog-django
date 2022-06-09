from re import A
from django.urls import path
from .views import BlogCreateView, BlogListView, BlogDetailView

app_name="blog"

urlpatterns = [
    path('', BlogListView.as_view(), name="home"),
    path('create/', BlogCreateView.as_view(), name="create"),
    path('<int:pk>/', BlogDetailView.as_view(), name="detail")
]