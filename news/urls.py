from django.urls import path
from news import views as news_views

app_name = 'news'

urlpatterns = [
    path(
        '',
        news_views.NewsItemListView.as_view(),
        name='newslist'
    )
]
