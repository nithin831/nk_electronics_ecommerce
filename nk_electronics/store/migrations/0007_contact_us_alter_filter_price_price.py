# Generated by Django 5.0 on 2024-02-22 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_images_image_alter_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('subject', models.CharField(max_length=300)),
                ('message', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='filter_price',
            name='price',
            field=models.CharField(choices=[('1000 to 10000', '1000 to 10000'), ('10000 to 200000', '10000 to 20000'), ('20000 to 30000', '20000 to 30000'), ('30000 to 40000', '30000 to 40000'), ('40000 to 50000', '40000 to 50000'), ('50000 and More', '50000 and More')], max_length=100),
        ),
    ]