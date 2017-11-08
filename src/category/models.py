from __future__ import unicode_literals

from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    post_number = models.IntegerField()

    def __unicode__(self):
        return str(self.category_name)

    def __str__(self):
        return str(self.category_name)
