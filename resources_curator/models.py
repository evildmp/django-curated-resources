from django.db import models

from mptt.models import MPTTModel, TreeForeignKey

class Resource(models.model):
    title = models.CharField(
        max_length=255,
        help_text=u"e.g. Interviewing Students - A Refresher for Admissions Tutors")
    short_title = models.CharField(
        max_length=255,  
        null=True, blank=True,
        help_text= u"e.g. Interviewing Students refresher (if left blank, will be copied from Title)")
    description = models.TextField(
        verbose_name=u"Description",
        null=False, blank=False, 
        help_text="Use carriage returns for paragraphs, and asterisks for list items")
    published = models.BooleanField(
        default=False, 
        verbose_name=_(u"Is published"), 
        db_index=True,
        help_text=_(u"Select when ready to be published"))
    related_to = models.ManyToManyField(
        Resource, 
        help_text=u"Similar resources - use judiciously", 
        null=True, blank=True)
    suitable_for = models.ManyToManyField(
        Audience,
        null=True, blank=True)
    topics = models.ManyToManyField(
        Topic,
        null=True, blank=True.
        help_text=_(u"Informal mapping of this resource to topics")
        )
    domains = models.ManyToManyField(
        Topic,
        null=True, blank=True,
        help_text=_(u"Formal mapping of this resource to a domain or domains"))
    resource_type = models.ForeignKey(
        ResourceType, 
        )
        
class ResourceType(models.model):
    resource_type = models.CharField(
        max_length=255,
        unique = True,
        help_text=u"e.g. 'PDF', 'training course', 'online documentation'")

class Audience(models.model):
    name = models.CharField(
        max_length=255,
        help_text=u"e.g. '")
    
class Topic(models.model):
    name = models.CharField(
        max_length=255,
        help_text=u"e.g. '")

class Domain(MPTTModel):
    name = models.CharField(
        max_length=255,
        help_text=u"e.g. '")
    parent = TreeForeignKey(
        'self', 
        null=True, blank=True, 
        related_name='children')


