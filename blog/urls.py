from re import A
from django.urls import path
from .views import BlogCreateView, BlogListView, BlogDetailView, BlogUpdateView

app_name="blog"

urlpatterns = [
    path('', BlogListView.as_view(), name="home"),
    path('create/', BlogCreateView.as_view(), name="create"),
    path('<int:pk>/', BlogDetailView.as_view(), name="detail"),
    path('<int:pk>/update/', BlogUpdateView.as_view(), name="update")
]