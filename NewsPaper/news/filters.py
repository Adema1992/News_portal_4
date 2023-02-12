from django_filters import FilterSet, DateTimeFilter, ModelChoiceFilter
from .models import Post
from django.forms import DateTimeInput

class NewsFilter(FilterSet):
    added_after = DateTimeFilter(
        field_name='dateCreation',
        label='Date',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},

        ),
    )



    class Meta:
       model = Post
       fields = {
           'title': ['exact'],
           'postCategory': ['exact'],
       }


