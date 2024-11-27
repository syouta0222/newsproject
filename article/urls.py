from django.urls import path
from . import views

app_name = 'article'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('mypage/', views.MypageView.as_view(), name ='mypage'),
    path('post/', views.CreateArticleView.as_view(), name='post'),
    path('post_done/', views.PostSuccessView.as_view(), name='post_done'),
    path('articles/<int:category>', views.CategoryView.as_view(), name = 'articles_cat'),
    path('user-list/<int:user>', views.UserView.as_view(), name = 'user_list'),
    path('article-detail/<int:pk>', views.DetailView.as_view(), name = 'article_detail'),
    path('article/<int:pk>/delete/', views.ArticleDeleteView.as_view(), name = 'article_delete'),
    path('contact/', views.ContactView.as_view(), name = 'contact'),
]
