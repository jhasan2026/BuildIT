from django.urls import path, include
from . import views
from .views import (PostListView, PostDetailView, PostCreateView, PostUpdateView,PostDeleteView,  RentPostListView,
                    MortgagePostListView, PostPayView, MyPostListView,MortgageCardView,RentCardView,PostSearchView)
urlpatterns = [
    path('',PostListView.as_view(),name='posts-home'),
    path('search/', PostSearchView.as_view(), name='post_search'),
    path('rentPost/',RentPostListView.as_view(),name='rent-posts'),
    path('morgagePost/',MortgagePostListView.as_view(),name='mortgage-posts'),
    path('morgagePost/<int:pk>/', MortgageCardView.as_view(), name='mortgage-card'),
    path('rentPost/<int:pk>/', RentCardView.as_view(), name='rent-card'),
    path('about/',views.about,name='posts-about'),
    path('prediction/', views.prediction, name='prediction'),
    path("selfPosts/", MyPostListView.as_view(), name='self-posts'),
    # path("user/<str:username>", UserPostListView.as_view(), name='user-posts'),
    path("post/<int:pk>/", PostDetailView.as_view(), name='post-detail'),
    path("post/<int:pk>/payment", PostPayView.as_view(), name='post-pay'),
    path('post/<int:post_id>/review/', views.add_review, name='add_review'),
    path("post/new/", PostCreateView, name='post-create'),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name='post-update'),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name='post-delete'),


]