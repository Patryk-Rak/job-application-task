from django.urls import reverse
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Example of simple validator
def price_validator(value):
    if value <= 0:
        raise ValidationError(
            _(f'{value} Price is too small, put number more than 0'),
            params={'value': value},
        )


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    ordering = models.PositiveSmallIntegerField(default=1, editable=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('ordering',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('offers:offer_list_by_category',
                       args=[self.slug])


class Offer(models.Model):
    category = models.ForeignKey(Category, related_name='categories', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, db_index=True)
    description = models.TextField(max_length=500, blank=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='offers/%Y/%m/%d',
                              blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[price_validator])
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('title',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('offers:offer_detail',
                       args=[self.id, self.slug])
