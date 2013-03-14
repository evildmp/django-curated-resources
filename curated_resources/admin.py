from django.contrib import admin
from polls.models import Resource, ResourceType, Audience, Topic, Domain

admin.site.register(Resource)
admin.site.register(ResourceType)
admin.site.register(Audience)
admin.site.register(Topic)
admin.site.register(Domain)
