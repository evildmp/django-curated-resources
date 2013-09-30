import django_filters     

from .models import Resource

class ResourceFilter(django_filters.FilterSet):
    class Meta:
        model = Resource
        fields = [
            'title', 
            'description', 
            'domains', 
            'topics', 
            'resource_type', 
            'suitable_for', 
            ]
