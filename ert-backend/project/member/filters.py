import django_filters
from .models import Member


class MemberFilter(django_filters.rest_framework.FilterSet):
    city = django_filters.CharFilter(field_name='user__city')

    class Meta:
        model = Member
        fields = ()
