from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import index,login_view,dashboard, logout_view,register,borrow_book,delete_borrow,edit_borrow,view_borrowed,search_books


urlpatterns = [
    path('', index),
    path('login/', login_view),
    path('dashboard/', dashboard),
    path('logout/', logout_view, name="logout"),
    path('register/', register, name="register"),
    path('dashboard/borrow/', borrow_book, name="borrow"),
    path('dashboard/borrow/delete/<int:id>', delete_borrow, name="deleteBorrow"),
    path('dashboard/borrow/edit/<int:id>', edit_borrow, name="editBorrow"),
    path('dashboard/borrow/viewBooks/', view_borrowed, name="viewBorrow"),
    path('dashboard/search/', search_books, name="search"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)