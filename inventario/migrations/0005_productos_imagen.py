# Generated by Django 4.2.5 on 2023-10-16 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0004_alter_productos_categoria_fk'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='img_inventario'),
        ),
    ]
