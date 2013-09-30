from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple

from mptt.forms import TreeNodeMultipleChoiceField

from treeadmin.admin import TreeAdmin

from widgetry.tabs.admin import ModelAdminWithTabs
from widgetry import fk_lookup
# from widgetry.views import search 

from arkestra_utilities.admin_mixins import AutocompleteMixin, InputURLMixin
from links import schema

from curated_resources.models import Resource, ResourceType, Audience, Topic, Domain


class ResourceAdminForm(InputURLMixin):
    # disabled: https://github.com/django-mptt/django-mptt/issues/255
    # domains = TreeNodeMultipleChoiceField(
    #     queryset=Domain.objects.all(),
    #     level_indicator=unichr(0x00A0) * 2,
    #     widget=FilteredSelectMultiple(
    #         "Domains",
    #         is_stacked=False,       
    #         )
    #     )

    def __init__(self, *args, **kwargs):
        super(ResourceAdminForm, self).__init__(*args, **kwargs)
        if self.instance.pk is not None and self.instance.destination_content_type:
            destination_content_type = self.instance.destination_content_type.model_class()
        else:
            destination_content_type = None
        # look up the correct widget from the content type
        widget = fk_lookup.GenericFkLookup(
            'id_%s-destination_content_type' % self.prefix,
             destination_content_type,
             )
        self.fields['destination_object_id'].widget = widget
        self.fields['destination_content_type'].widget.choices = schema.content_type_choices()

from django.contrib.admin import SimpleListFilter


class ResourceAdmin(ModelAdminWithTabs, AutocompleteMixin):
    form = ResourceAdminForm
    related_search_fields = ['destination_content_type']
    filter_horizontal = (
        'related_to',
        'suitable_for',
        'topics',
        'domains',
        'curators'
        )
    list_filter = ('resource_type', 'published')
    list_display = ('title', 'published')
    prepopulated_fields = {"slug": ("title",)}
    tabs = [
        ('Description', {'fieldsets': [
            [None, {'fields': [('title', 'short_title'), ('resource_type', 'published'), 'description',]}],
            ["Link to the resource",{'fields': [('destination_content_type', 'destination_object_id',)]}],
            ["Duration and cost",{'fields': [('duration', 'cost',)]}]
        ]}),
        ('Audience', {'fieldsets': [[None,{'fields': ['suitable_for',]}]]}),
        ('Domains', {'fieldsets': [[None,{'fields': ['domains',]}]]}),
        ('Topics', {'fieldsets': [[None,{'fields': ['topics',]}]]}),
        ('Related items', {'fieldsets': [[None,{'fields': ['related_to',]}]]}),
        ('Curators', {'fieldsets': [[None,{'fields': ['curators',]}]]}),
        ('Advanced options', {'fieldsets': [[None,{'fields': ['slug',]}]]}),
    ]

class TreeRoots(SimpleListFilter):
    title = _('domain scheme')
    parameter_name = 'tree'

    def lookups(self, request, model_admin): 
        roots = Domain.objects.filter(parent=None)
        t = [(root.tree_id, root.name) for root in roots]
        return t

    def queryset(self, request, queryset):
        if self.value():  
            return queryset.filter(tree_id = self.value())

        
class DomainAdmin(TreeAdmin):
    enable_object_permissions = False
    jquery_use_google_cdn = True
    search_fields = ('name',)
    list_display = ('name', 'id_code', 'number_of_resources', 'number_of_children')
    list_filter = (TreeRoots,)
    filter_horizontal = ('curators',)

   
class TopicAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'number_of_resources')
    filter_horizontal = ('curators',)
   
class ResourceTypeAdmin(admin.ModelAdmin):
    search_fields = ('resource_type',)
    list_display = ('resource_type', 'number_of_resources')

class AudienceAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'number_of_resources')
    filter_horizontal = ('curators',)
    
admin.site.register(Resource, ResourceAdmin)
admin.site.register(ResourceType, ResourceTypeAdmin)
admin.site.register(Audience, AudienceAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Domain, DomainAdmin)
