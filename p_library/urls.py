from django.contrib.auth import views
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from .views import index, AuthorEdit, AuthorList, BookEdit, BookList, FriendEdit, FriendList, PublisherList, signup
from django.urls import reverse_lazy
from p_library import views
from allauth.account.views import login, logout
    
app_name = 'p_library'
urlpatterns = [
    path('', index, name='home'),
    path('login/', login, name='login'),  
    path('logout/', logout, name='logout'),
    path('signup/', signup, name='signup'),  
    path('book/', BookList.as_view(), name='book_list'),
    path('book/add',  BookEdit.as_view(), name='book_add'),
    path('author/add/', AuthorEdit.as_view(), name='author_add'),
	path('author/', AuthorList.as_view(), name='author_list'),
    path('friend/add/', FriendEdit.as_view(), name='friend_add'),
    path('friend/', FriendList.as_view(), name='friend_list'),
    path('publisher/', PublisherList.as_view(), name='publisher_list'),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)