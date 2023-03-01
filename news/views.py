from django.views import generic
from news.models import NewsItem

class NewsItemListView(generic.ListView):
    template_name = 'news/news_list.html'
    model = NewsItem
    context_object_name = 'newsitems'
