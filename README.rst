django-centralniak-slugfield
============================

This tiny project adds new Django field type ``CentralniakSlugField`` that automatically creates and/or updates 
slug on save. The slug method supports far more regional characters then the core Django one (yes, cyrillic 
alphabet is supported).

Project was somewhat inspired by `Doctrine ORM's approach <http://www.doctrine-project.org/documentation/manual/1_0/en/behaviors:core-behaviors:sluggable>`_ to slugs.

Features:
---------

1. You can choose which fields to populate a slug form (single or multifield slug)
2. You can choose if slug should be updated on record update or only on creation 
3. Possibility to make slugs unique per given expression only (for example given date)

Installation:
-------------

* Put ``django_centralniak_slugfield`` in your ``INSTALLED_APPS``

Usage:
------

:: 
  
  from django_centralniak_slugfield import CentralniakSlugField 
  
  class MyModel(models.model):
      fieldname1 = models.CharField(max_length=12)
      fieldname2 = models.CharField(max_length=34)
      other_model = models.ForeignKey(OtherModel)
      slug = CentralniakSlugField(populate_from=['fieldname1', 'fieldname2'], update_on_edit=False, unique_for=['other_model'])

Kudos:
------

Samuel Adam for the slughifi module (couldn't find it online anymore)