from django.urls import path
from .views import NewsList, NewsDetail, multiply, PostSearch, NewsCreate, NewsUpdate, NewsDelete

urlpatterns = [
   path('multiply/', multiply),
   path('', NewsList.as_view(), name='news_list'),
   path('<int:pk>', NewsDetail.as_view(),name='news_detail'),
   path('search/', PostSearch.as_view()),
   path('create/', NewsCreate.as_view(), name='news_create'),
   path('<int:pk>/update/', NewsUpdate.as_view(), name='news_update'),
   path('<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),

]