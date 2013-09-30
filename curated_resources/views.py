from django.http import HttpResponse 
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from .models import Resource

def index(request):
    latest_resources_list = Resource.objects.order_by('-id')[:5]  
    context = {'latest_resources_list': latest_resources_list,}
    return render(request, 'curated_resources/index.html', context)

def detail(request, resource_slug):
    print resource_slug
    resource = get_object_or_404(Resource, slug=resource_slug, published=True)
    return render(request, 'curated_resources/detail.html', {'resource': resource})
       
# from .filters import ResourceFilter
# def resource_list(request):
#     f = ResourceFilter(request.GET, queryset=Resource.objects.all())
#     return render(request, 'curated_resources/filtertemplate.html', {'filter': f})
     
from django_easyfilters import FilterSet

class ResourceFilterSet(FilterSet):
    fields = [
        'domains',
        'topics',
        'suitable_for'
        ]

    title_fields = ['domains', 'topics']


def resource_list(request):
    resources = Resource.objects.filter(published=True).order_by('title')

    search_fields = [
        {
            "field_name": "title",
            "field_label": "Title/description",
            "placeholder": "",
            "search_keys": [
                "title__icontains", 
                "short_title__icontains", 
                "description__icontains", 
                ],    
            },
        ]
    for search_field in search_fields:
        field_name = search_field["field_name"]
        if field_name in request.GET:
            query = request.GET[field_name]
            search_field["value"] = query
            
            q_object = Q()
            for search_key in search_field["search_keys"]:
                lookup = {search_key: query}
            q_object |= Q(**lookup)
            resources = resources.distinct().filter(q_object) 

    hidden_search_fields = []
    for key in ResourceFilterSet.fields:
        if key not in [search_field["field_name"] for search_field in search_fields]:
            for query_value in request.GET.getlist(key):
                # the field_name and query_value populate some <input> elements
                hidden_search_fields.append(
                    {
                        "field_name": key,
                        "value": query_value,                            
                    })
                    
    resourcesfilter = ResourceFilterSet(resources, request.GET)
    
    
    
    return render(request, "curated_resources/resourcelist.html", {
        'resources': resourcesfilter.qs,
        'resourcesfilter': resourcesfilter,
        "search_fields": search_fields,
        })
