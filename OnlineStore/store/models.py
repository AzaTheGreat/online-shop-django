from django.db import models
from django.utils.translation import gettext_lazy as _
from taggit.managers import TaggableManager
from taggit.models import GenericTaggedItemBase, TagBase


class ItemTag(TagBase):
    image = models.ImageField(
        upload_to='categories/',
        verbose_name='Image',
        blank=True
    )
    description = models.TextField(
        blank=True,
        verbose_name='Description',
        )

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")


class TaggedItem(GenericTaggedItemBase):
    tag = models.ForeignKey(
        ItemTag,
        on_delete=models.CASCADE,
        related_name="items",
        verbose_name='Category',
    )


class Item(models.Model):
    title = models.CharField(max_length=200, verbose_name='Title',)
    description = models.TextField(verbose_name='Description',)
    slug = models.CharField(
        unique=True,
        max_length=50,
    )
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Publication date',)
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name='New price',
    )
    old_price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name='Old price',
        blank=True,
        null=True,
    )
    image = models.ImageField(
        verbose_name='Image',
        upload_to='items/',
        blank=True,
    )
    is_available = models.BooleanField(
        default=True,
        verbose_name='Available',
    )
    tags = TaggableManager(through=TaggedItem, related_name="tagged_items", verbose_name='Category',)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-price']
        verbose_name = 'Item'
        verbose_name_plural = 'Items'
