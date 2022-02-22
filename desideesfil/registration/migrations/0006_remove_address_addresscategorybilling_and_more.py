# Generated by Django 4.0.2 on 2022-02-22 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0005_remove_address_addresscategory_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='addressCategoryBilling',
        ),
        migrations.RemoveField(
            model_name='address',
            name='addressCategoryDelivery',
        ),
        migrations.AddField(
            model_name='address',
            name='addressCategoryName',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='registration.addresscategory'),
            preserve_default=False,
        ),
    ]
