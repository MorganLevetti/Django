# Generated by Django 4.1.4 on 2022-12-21 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='band',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='listings.band'),
        ),
    ]
