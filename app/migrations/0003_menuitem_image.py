# Generated by Django 4.2.4 on 2023-08-06 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_cart_deliverycrew_order_alter_menuitem_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='image',
            field=models.CharField(default='', max_length=150, null=True),
        ),
    ]
