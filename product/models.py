from django.db import models
from utils.images import resize_image
from utils.random_generator import slugify_new


class Product(models.Model):
    name = models.CharField(max_length=255)
    short_description = models.TextField(max_length=255)
    long_description = models.TextField()
    marketing_price = models.FloatField()
    promotional_marketing_pricing = models.FloatField(default=0)
    Type = models.CharField(
        default='V',
        max_length=1,
        choices=(
            ('V', 'variação'),
            ('S', 'simples')
        )

    )
    main_image = models.ImageField(
        upload_to='product_image/%Y/%m',
        blank=True, null=True
    )
    additional_image_1 = models.ImageField(
        upload_to='product_image/%Y/%m',
        blank=True, null=True
    )
    additional_image_2 = models.ImageField(
        upload_to='product_image/%Y/%m',
        blank=True, null=True
    )
    additional_image_3 = models.ImageField(
        upload_to='product_image/%Y/%m',
        blank=True, null=True
    )
    slug = models.SlugField(
        unique=True,
        default=None, null=True,
        blank=True, max_length=255
    )

    visible = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs) -> None:
        if not self.main_image:
            self.visible = False

        if not self.slug:
            self.slug = slugify_new(self.name)

        current_main_image_name = str(self.main_image.name)
        super().save(*args, **kwargs)
        main_image_changed = False

        if self.main_image:
            main_image_changed = current_main_image_name != self.main_image.name    # noqa: E501

        if main_image_changed:
            resize_image(self.main_image, 900)

        return super().save(*args, **kwargs)
