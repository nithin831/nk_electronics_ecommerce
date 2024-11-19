# Generated by Django 5.0 on 2024-02-24 05:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_alter_contact_us_date'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('postalcode', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=200)),
                ('additional_info', models.TextField()),
                ('amount', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=200)),
                ('image', models.CharField(max_length=500)),
                ('quantity', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('total', models.CharField(max_length=100)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.order')),
            ],
        ),
    ]
