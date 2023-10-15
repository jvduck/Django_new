# Generated by Django 4.2.5 on 2023-10-12 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0002_alter_productos_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='productos',
            name='categoria_fk',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='inventario.categorias'),
            preserve_default=False,
        ),
    ]