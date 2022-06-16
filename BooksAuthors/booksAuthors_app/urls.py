from django.urls import path , include
from . import views

urlpatterns = [
    path('',views.index),
    path('addBook',views.addBook),
    path('book/<int:id>',views.book),
    path('addAuthor',views.addAuthor),
    path('author/<int:id>',views.author),
    path('authorToBook/<int:authorId>',views.authorToBook),
    path('bookToAuthor/<int:bookId>',views.bookToAuthor),
    path('authors',views.authors)
    # path('admin/', admin.site.urls),
]