from django.urls import path
from .views import myapp_home,root_page,portfolio

urlpatterns = [
    path("portfolio/",portfolio, name="portfolio"),
    path("",root_page, name="root_page"),
    path("",myapp_home)
]
