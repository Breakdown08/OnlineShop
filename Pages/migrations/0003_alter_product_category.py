# Generated by Django 4.1.5 on 2023-01-16 04:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0002_category_slug_childcategory_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='this_category_products', to='Pages.childcategory'),
        ),
    ]
