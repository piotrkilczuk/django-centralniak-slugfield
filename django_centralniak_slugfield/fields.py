from django.db.models import SlugField
import slughifi
from south.modelsinspector import add_introspection_rules


class CentralniakSlugField(SlugField):
    
    """Provide more handy support for slugs in models
    
    Usage:
    slug = CentralniakSlugField(populate_from=['fieldname1', 'fieldname2'], update_on_edit=False, unique_for=['fieldname3'])
    
    """
    
    description = __doc__
    populate_from = None
    update_on_edit = False
    unique_for = None
    
    def __init__(self, populate_from, update_on_edit=False, unique_for=None, *args, **kwargs):
        self.populate_from = populate_from
        self.update_on_edit = update_on_edit
        self.unique_for = unique_for
        super(CentralniakSlugField, self).__init__(*args, **kwargs)
    
    def __slugify(self, model_instance):
        "Slughifi is courtesy of Samuel Adam - samuel.adam@gmail.com"
        slug_sources = [getattr(model_instance, field) for field in self.populate_from]
        slug = slughifi.slughifi((' ').join(slug_sources))
        suffix_idx = 1
        # check for uniqueness
        lookup_kwargs = {
            self.attname: slug
        }
        exclude_kwargs = {}
        if self.unique_for:
            for unique_column in self.unique_for:
                lookup_kwargs[unique_column] = getattr(model_instance, unique_column)
        if model_instance.pk:
            exclude_kwargs['pk'] = model_instance.pk
        while model_instance.__class__.objects.exclude(**exclude_kwargs).filter(**lookup_kwargs).count() > 0:
            suffix_idx += 1
            slug = slughifi.slughifi((' ').join(slug_sources)) + '-%d' % suffix_idx
            lookup_kwargs[self.attname] = slug
        return slug
    
    def pre_save(self, model_instance, add):
        "Run just before a field is saved"
        current_value = super(CentralniakSlugField, self).pre_save(model_instance, add)
        if not current_value or self.update_on_edit:
            slug = self.__slugify(model_instance)
            return slug
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
        },
    ),
], ['django_centralniak_slugfield\.fields\.CentralniakSlugField'])