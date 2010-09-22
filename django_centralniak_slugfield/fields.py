from django.db.models import SlugField
import slughifi
from south.modelsinspector import add_introspection_rules


class CentralniakSlugField(SlugField):
    
    """Provide more handy support for slugs in models
    
    Usage:
    slug = CentralniakSlugField(populate_from=['fieldname1', 'fieldname2']
    
    """
    
    description = __doc__
    populate_from = None
    update_on_edit = False
    
    def __init__(self, populate_from, update_on_edit=False, *args, **kwargs):
        self.populate_from = populate_from
        self.update_on_edit = update_on_edit
        super(CentralniakSlugField, self).__init__(*args, **kwargs)
    
    def __slugify(self, model_instance):
        "Courtesy of Samuel Adam"
        slug_sources = [getattr(model_instance, field) for field in self.populate_from]
        return slughifi.slughifi((' ').join(slug_sources))
    
    def pre_save(self, model_instance, add):
        "Run just before a field is saved"
        current_value = super(CentralniakSlugField, self).pre_save(model_instance, add)
        if not current_value or self.update_on_edit:
            return self.__slugify(model_instance)
        else:
            return current_value


add_introspection_rules([
    (
        (CentralniakSlugField,),
        [],
        {
            "max_length": ["max_length", {"default": 50}],
            "db_index": ["db_index", {"default": True}],
            "populate_from": ["populate_from", {"default": []}],
            "update_on_edit": ["update_on_edit", {"default": False}],
        }
    ),
], 'django_centralniak_slugfield\.fields\.CentralniakSlugField')