# Generated by Django 5.0 on 2024-02-19 11:42

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('image', models.ImageField(upload_to='Product_images/img')),
                ('name', models.CharField(max_length=500)),
                ('price', models.IntegerField()),
                ('condition', models.CharField(choices=[('New', 'New'), ('Old', 'Old')], max_length=100)),
                ('tax', models.IntegerField(null=True)),
                ('packing_cost', models.IntegerField(null=True)),
                ('information', models.TextField()),
                ('description', models.TextField()),
                ('stocks', models.CharField(choices=[('IN STOCK', 'IN STOCK'), ('OUT OF STOCK', 'OUT OF STOCK')], max_length=100)),
                ('status', models.CharField(choices=[('Publish', 'Publish'), ('Draft', 'Draft')], max_length=100)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('Categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.category')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.brand')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.color')),
                ('filter_price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.filter_price')),
            ],
        ),
    ]
