# Generated by Django 4.2.5 on 2023-09-07 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_alter_order_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='size',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]