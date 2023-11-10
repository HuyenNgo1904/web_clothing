from django.db import models

from polls import CompositeAutoField


# Create your models here.
class UserStatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    create_date = models.DateTimeField(auto_now_add=True, editable=False)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user_status'


class Role(models.Model):
    id = models.BigAutoField(primary_key=True),
    name = models.CharField(max_length=255),
    create_date = models.DateTimeField(auto_now_add=True, editable=False)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'role'


class User(models.Model):
    id = CompositeAutoField(
        prefix='UE',
        max_length=15,
        primary_key=True

    )
    first_name = models.CharField(max_length=255),
    last_name = models.CharField(max_length=255),
    email = models.CharField(max_length=255),
    phone_number = models.CharField(max_length=12),
    customer_status = models.ForeignKey(UserStatus, on_delete=models.CASCADE, related_name='user'),
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='role'),
    create_date = models.DateTimeField(auto_now_add=True, editable=False)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user'


class ProductType(models.Model):
    id = models.BigAutoField(primary_key=True),
    name = models.CharField(max_length=255),
    create_date = models.DateTimeField(auto_now_add=True, editable=False)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'product_type'


class ProductStatus(models.Model):
    id = models.BigAutoField(primary_key=True),
    name = models.CharField(max_length=255),
    create_date = models.DateTimeField(auto_now_add=True, editable=False)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'product_status'


class SkuItem(models.Model):
    id = models.BigAutoField(primary_key=True),
    name = models.CharField(max_length=255),
    invalid = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True, editable=False)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'sku_item'


class Product(models.Model):
    id = CompositeAutoField(
        prefix='PD',
        max_length=15,
        primary_key=True

    )
    name = models.CharField(max_length=255),
    description = models.TextField(),
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE, related_name='product-type'),
    product_status = models.ForeignKey(ProductStatus, on_delete=models.CASCADE, related_name='product-status'),
    note = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True, editable=False)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'product'


class ProductImage(models.Model):
    id = models.BigAutoField(primary_key=True),
    sort_no = models.IntegerField(),
    file_name = models.CharField(255),
    create_date = models.DateTimeField(auto_now_add=True, editable=False)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'product_image'


class SkuSetItem(models.Model):
    id = models.BigAutoField(primary_key=True),
    sku_item = models.ForeignKey(SkuItem, on_delete=models.CASCADE, related_name='sku_item'),
    name = models.CharField(max_length=255),
    invalid = models.BooleanField(default=False),
    create_date = models.DateTimeField(auto_now_add=True, editable=False)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'sku_set_item'


class ProductSku(models.Model):
    id = CompositeAutoField(
        prefix='SK',
        max_length=15,
        primary_key=True

    )
    sku_set_item1 = models.ForeignKey(SkuSetItem, on_delete=models.CASCADE, related_name='sku-set-item'),
    sku_set_item2 = models.ForeignKey(SkuSetItem, on_delete=models.CASCADE, related_name='sku-set-item'),
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE),
    stock = models.IntegerField(),
    price = models.IntegerField()
    create_date = models.DateTimeField(auto_now_add=True, editable=False)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'product_sku'


