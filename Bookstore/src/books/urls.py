from django.urls import path
from .views import home, BookListView, BookDetailView


app_name = 'books' 

urlpatterns = [
    path('', home),
    path('list/', BookListView.as_view(), name='list'),
    path('list/<pk>', BookDetailView.as_view(), name='detail'),
]