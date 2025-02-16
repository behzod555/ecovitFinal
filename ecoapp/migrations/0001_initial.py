# Generated by Django 4.0.5 on 2022-10-11 08:30

import ckeditor.fields
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
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение')),
                ('ordering', models.IntegerField(default=0)),
                ('is_featured', models.BooleanField(default=False)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='ecoapp.category')),
            ],
            options={
                'verbose_name_plural': 'Категории',
                'ordering': ('ordering',),
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True, verbose_name='Имя')),
                ('email', models.CharField(max_length=200)),
                ('tel', models.CharField(max_length=200, verbose_name='Номер телефона')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Клиенты',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ordered', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата')),
                ('complete', models.BooleanField(blank=True, default=False, null=True, verbose_name='Заказанно')),
                ('paid', models.BooleanField(blank=True, default=False, null=True, verbose_name='Оплачено')),
                ('delivered', models.BooleanField(blank=True, default=False, null=True, verbose_name='Доставлено')),
                ('order_key', models.CharField(max_length=25, verbose_name='Имя:')),
                ('transaction_id', models.CharField(max_length=100, null=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ecoapp.customer', verbose_name='Клиент')),
            ],
            options={
                'verbose_name': 'Заказы',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название продукта')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('description', ckeditor.fields.RichTextField(blank=True, verbose_name='Описание:')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение')),
                ('novinki', models.BooleanField(default=False, verbose_name='Новинки')),
                ('popularnye', models.BooleanField(default=False, verbose_name='Популарные')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='ecoapp.category')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='variants', to='ecoapp.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Продукты',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=0, null=True, verbose_name='Количество')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ecoapp.order', verbose_name='ID заказа')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ecoapp.product', verbose_name='Название товара')),
            ],
            options={
                'verbose_name': 'Заказанные товары',
                'verbose_name_plural': 'Заказанные товары',
            },
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Имя:')),
                ('email', models.CharField(blank=True, max_length=200, null=True, verbose_name='Email:')),
                ('phone', models.CharField(blank=True, max_length=200, null=True, verbose_name='Номер телефона:')),
                ('phoneAdd', models.CharField(blank=True, max_length=200, null=True, verbose_name='Доп. номер телефона:')),
                ('address', models.CharField(blank=True, max_length=200, null=True, verbose_name='Адрес:')),
                ('time', models.CharField(blank=True, max_length=200, null=True, verbose_name='Время:')),
                ('date', models.CharField(blank=True, max_length=200, null=True, verbose_name='Дата:')),
                ('payment', models.CharField(blank=True, max_length=200, null=True, verbose_name='Способ оплаты:')),
                ('comment', models.CharField(blank=True, max_length=200, null=True, verbose_name='Коментарии:')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ecoapp.customer', verbose_name='Клиент')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ecoapp.order', verbose_name='ID заказа')),
            ],
            options={
                'verbose_name': 'Информации о заказе',
                'verbose_name_plural': 'Информации о заказе',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=2500)),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
                ('approved', models.BooleanField(default=False, verbose_name='Подтвердить')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ecoapp.product', verbose_name='Название товара')),
            ],
        ),
    ]
