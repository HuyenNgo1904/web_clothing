import math
from django.db import models
from django.utils import timezone
__all__ = [
    'CompositeAutoField',
]


class CompositeAutoField(models.CharField):
    defaults = dict(unique=True, editable=False, db_index=True)

    def __init__(self, *args, prefix='CC', **kwargs):
        self.prefix = prefix
        kwargs.update(self.defaults)
        super().__init__(*args, **kwargs)

    def generate_pk(self, prefix):
        dt = timezone.now()
        seq_number = int(math.floor(dt.timestamp() * 1000))
        return f'{prefix}{seq_number}'

    def pre_save(self, model_instance, add):
        if add and self.prefix:
            value = self.generate_pk(self.prefix)
            setattr(model_instance, self.attname, value)
            return value

        return super(CompositeAutoField, self).pre_save(model_instance, add)