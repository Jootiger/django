from django.urls import path
from api import views

app_name = "api"

urlpatterns = [
        #도서목록 http://127.0.0.0:8000/api/v1/books/1
        path('v1/books/', views.book_list, name='book_list'),
]
