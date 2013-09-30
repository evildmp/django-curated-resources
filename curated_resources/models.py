import datetime
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField

from links.models import LinkMethodsMixin

class Resource(models.Model):
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
        help_text="Use carriage returns for paragraphs, and asterisks for list items.")
    resource_type = models.ManyToManyField(
        "ResourceType", 
        verbose_name = "Type",
        related_name="resources",
        null=True, blank=True,
        )
    published = models.BooleanField(
        default=False, 
        verbose_name = u"Published", 
        db_index=True,
        help_text=u"Select when ready to be published")
    cost = models.CharField(
        max_length=255,  
        null=True, blank=True,
        )
    duration = models.CharField(
        max_length=255,  
        null=True, blank=True,
        help_text= u"Don't use abbreviations for <em>day</em>, <em>hour</em> etc.")
    related_to = models.ManyToManyField(
        'self', 
        help_text=u"Similar resources - use judiciously.", 
        null=True, blank=True)
    suitable_for = models.ManyToManyField(
        "Audience",
        related_name="resources",
        null=True, blank=True)
    topics = models.ManyToManyField(
        "Topic",
        null=True, blank=True,
        help_text=u"<strong>Informal mapping</strong> of this resource to topics.",
        related_name="resources",
        )
    curators = models.ManyToManyField(
        User,
        null=True, blank=True,
        help_text=u"The web editors responsible for maintaining this resource",
        related_name="curated_resource_resources",
        )
    domains = TreeManyToManyField(
        "Domain",
        null=True, blank=True,
        help_text=u"<strong>Formal mapping</strong> of this resource to a domain or domains.",
        related_name="resources", 
        )        
    slug = models.SlugField(
        max_length=75,
        unique=True,
        default=datetime.datetime.now())
    destination_content_type = models.ForeignKey(
        ContentType,
        blank = True, null = True, 
        verbose_name="Type", 
        related_name = "links_to_%(class)s") 
    destination_object_id = models.PositiveIntegerField(
        verbose_name="Item",
        blank = True, null = True, 
        )
    destination_content_object = generic.GenericForeignKey('destination_content_type', 'destination_object_id')

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('curated_resources.views.detail', args=[self.slug])              
        
    def related_resources(self):
        return self.related_to.all().exclude(id=self.id, published=False)              
        
class ResourceType(models.Model):
    resource_type = models.CharField(
        max_length=255,
        unique = True,
        help_text=u"e.g. 'PDF', 'training course', 'online documentation'")

    description = models.TextField(
        verbose_name=u"Description",
        null=True, blank=True, 
        help_text="Use carriage returns for paragraphs, and asterisks for list items")

    def get_absolute_url(self):
        return reverse('curated_resources.views.detail', args=[self.slug])              

    def __unicode__(self):
        return self.resource_type

    def number_of_resources(self):
        return self.resources.count()   
    number_of_resources.short_description = "Resources"


class Audience(models.Model):
    name = models.CharField(
        max_length=255,
        help_text=u"e.g. 'Undergraduates', 'Post-doctoral fellows'")
    
    description = models.TextField(
        verbose_name=u"Description",
        null=True, blank=True, 
        help_text="Use carriage returns for paragraphs, and asterisks for list items")

    curators = models.ManyToManyField(
        User,
        null=True, blank=True,
        help_text=u"The web editors responsible for maintaining this Audience category",
        related_name="curated_resource_audiences",
        )

    def __unicode__(self):
        return self.name

    def number_of_resources(self):
        return self.resources.count()   
    number_of_resources.short_description = "Resources"
        
        
class Topic(models.Model):
    name = models.CharField(
        max_length=255,
        help_text=u"e.g. 'Time-management', 'Health & safety'")

    description = models.TextField(
        verbose_name=u"Description",
        null=True, blank=True, 
        help_text="Use carriage returns for paragraphs, and asterisks for list items")

    curators = models.ManyToManyField(
        User,
        null=True, blank=True,
        help_text=u"The web editor responsible for maintaining this Topic",
        related_name="curated_resource_topics",
        )

    def __unicode__(self):
        return self.name

    def number_of_resources(self):
        return self.resources.count()   
    number_of_resources.short_description = "Resources"


class Domain(MPTTModel):
    name = models.CharField(
        max_length=255,
        help_text=u"Use only formal schemes")
        
    id_code = models.CharField(
        max_length=255,
        null=True, blank=True, 
        help_text=u"Number/letter id")

    description = models.TextField(
        verbose_name=u"Description",
        null=True, blank=True, 
        help_text="Use carriage returns for paragraphs, and asterisks for list items")
        
    parent = TreeForeignKey(
        'self', 
        null=True, blank=True, 
        related_name='children',
        )

    curators = models.ManyToManyField(
        User,
        null=True, blank=True,
        help_text=u"The web editor responsible for maintaining this Domain",
        related_name="curated_resource_domains",
        )

    def number_of_children(self):
        return self.get_descendant_count()
    number_of_children.short_description = "Sub-domains"
    
    def number_of_resources(self):
        return self.resources.count()   
    number_of_resources.short_description = "Resources"
    
    def __unicode__(self):
        return self.name


