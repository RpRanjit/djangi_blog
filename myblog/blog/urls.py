from django.urls import path
from .views import blog_list, blog_detail, post_like, about_us, contact, search, profile_view, create_post, delete_post, edit_post, posts_by_category


urlpatterns = [
    path('', blog_list, name = 'list'),
    path('posts/<int:pk>/', blog_detail, name = 'detail'),
    path('like_posts/<int:pk>/', post_like, name = 'like'),
    path('about_us/', about_us, name = 'about_us' ),
    path('contact/', contact, name = 'contact' ),
    path('posts/search', search, name = 'search'),

    path('category/<str:category_name>/', posts_by_category, name='posts_by_category'),

    path('profile/', profile_view, name= 'profile'),
    path('create-post/', create_post, name = 'create_post'),
    path('edit-post/<int:pk>/', edit_post, name = 'edit_post'),
    path('delete-post/<int:pk>/', delete_post, name= 'delete_post')
]
