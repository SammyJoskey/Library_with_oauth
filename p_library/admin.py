from django.contrib import admin
from p_library.models import Book, Author, Publisher, Friend, UserProfile


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_author', 'publisher', 'display_img')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'birth_year', 'country')

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', )

@admin.register(Friend)
class FriendsAdmin(admin.ModelAdmin):
    list_display = ('name', 'books_given', 'date')

@admin.register(UserProfile)
class UserProfilesAdmin(admin.ModelAdmin):
    list_display = ('user', 'age')