from django.urls import path
from .views import NewsList, NewsDetail, SearchList, PostDetailView, PostCreateView, PostDeleteView, PostUpdateView

urlpatterns = [
    path('', NewsList.as_view()),
    path('<int:pk>', NewsDetail.as_view()),
    path('search/', SearchList.as_view()),
    path('news/<int:pk>/', PostDetailView.as_view(), name='news_detail'),
    path('news/add/', PostCreateView.as_view(), name='news_create'),
    path('news/<int:pk>/edit/', PostUpdateView.as_view(), name='news_create'),
    path('news/delete/<int:pk>/',PostDeleteView.as_view(), name='news_delete'),

]