# Generated by Django 3.1.3 on 2020-12-08 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0006_auto_20201207_2143'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(default=None, max_length=200, unique=True)),
                ('adres', models.CharField(db_index=True, max_length=300)),
                ('image', models.ImageField(blank=True, upload_to='products/%Y/%m/%d')),
                ('bonus', models.FloatField(db_index=True, max_length=3)),
                ('available', models.BooleanField(default=True)),
                ('description', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='offer.category')),
            ],
            options={
                'ordering': ('name',),
                'index_together': {('id', 'slug')},
            },
        ),
        migrations.DeleteModel(
            name='Offers',
        ),
    ]
