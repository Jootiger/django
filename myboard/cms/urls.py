from django.urls import path
#from django.conf.urls import url

#from cms.views import *  #클래스있을 때 참조 방법
from cms import views #메소드를 참조하는 방법

app_name = 'cms'

urlpatterns = [
    #book_list
    path('book/', views.book_list, name='book_list'),
    #book_add
    path('book/add/', views.book_edit, name='book_add'),
    #book_edit
    path('book/modify/<int:book_id>/', views.book_edit, name='book_modify'),
    #book_remove
    path('book/delete/<int:book_id>/', views.book_remove, name='book_remove'),

    #impression_list
    path('impression/<int:book_id>/', views.ImpressionList.as_view(), name='impression_list'),
    #book_add
    path('impression/add/<int:book_id>/', views.impression_edit, name='impression_add'),
    #book_edit
    path('impression/modify/<int:book_id>/<int:impression_id>/', views.impression_edit,
        name='impression_modify'),
    #book_remove
    path('impression/delete/<int:book_id>/<int:impression:id>/', views.impression_remove,
        name='impression_remove'),


]
