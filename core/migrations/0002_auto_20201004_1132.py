# Generated by Django 3.1.1 on 2020-10-04 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(max_length=120, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.category'),
        ),
    ]
