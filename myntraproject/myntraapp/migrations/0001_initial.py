# Generated by Django 5.0.2 on 2024-02-09 04:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('productid', models.IntegerField(primary_key=True, serialize=False)),
                ('productname', models.CharField(max_length=55)),
                ('category', models.CharField(choices=[('glass', 'glass'), ('Cloths', 'Cloths'), ('Shoes', 'Shoes'), ('Electronics', 'Electronics')], default='', max_length=50)),
                ('desc', models.TextField(max_length=100)),
                ('price', models.FloatField()),
                ('photos', models.ImageField(upload_to='images')),
                ('userid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('orderid', models.IntegerField(primary_key=True, serialize=False)),
                ('qty', models.PositiveIntegerField(default=0)),
                ('userid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('productid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myntraapp.product')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.PositiveIntegerField(default=0)),
                ('userid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('productid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myntraapp.product')),
            ],
        ),
    ]
