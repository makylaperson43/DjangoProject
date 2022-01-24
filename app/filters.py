import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class OrderFilter(django_filters.FilterSet):
	date_made = DateFilter(field_name="date_made", lookup_expr='gte')
	date_deleted = DateFilter(field_name="date_made", lookup_expr='lte')
	note = CharFilter(field_name='note', lookup_expr='icontains')


class Meta:
	model = Book
	fields = '__all__'
	exclude = ['person', 'date_made'] 