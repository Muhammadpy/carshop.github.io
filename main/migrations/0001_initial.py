# Generated by Django 3.2.8 on 2022-04-06 09:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('reg_date', models.DateField(auto_now_add=True)),
                ('products_qty', models.PositiveIntegerField(default=0, editable=False)),
            ],
            options={
                'verbose_name': 'Kategoriya',
                'verbose_name_plural': 'Kategoriyalar',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='dssdf sdjdsjfskdfsdfs dshfj', max_length=355, verbose_name='Tovar nomi')),
                ('text', models.TextField(default="Text yo'q", max_length=8000, verbose_name='Tovar xaqida')),
                ('view', models.PositiveIntegerField(default=0, editable=False, verbose_name="Ko'rishlar soni")),
                ('likes', models.PositiveIntegerField(default=0, editable=False)),
                ('dislikes', models.PositiveIntegerField(default=0, editable=False)),
                ('image', models.ImageField(upload_to='')),
                ('reg_date', models.DateField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.category')),
            ],
            options={
                'verbose_name': 'Maqola',
                'verbose_name_plural': 'Maqolalar',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('reg_date', models.DateField(auto_now_add=True)),
                ('likes', models.PositiveIntegerField(default=0)),
                ('dislikes', models.PositiveIntegerField(default=0)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.product')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('incomment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.comment')),
            ],
        ),
    ]
