# Generated by Django 4.1.7 on 2023-02-20 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0009_alter_itemorder_item_alter_itemorder_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='prduct_id',
            new_name='product_id',
        ),
    ]