# Generated by Django 5.0 on 2024-02-06 13:53

import base.models
import django.contrib.gis.db.models.fields
import django.contrib.gis.geos.point
import django.core.validators
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Clients_and_Products', '0001_initial'),
        ('Human_Resources', '0001_initial'),
        ('Receipts', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medium',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='MediumTwo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='OrderEnvoy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.CharField(max_length=50)),
                ('address', models.CharField(default='address', max_length=100)),
                ('phonenumber', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='DZ')),
                ('products_num', models.IntegerField(default=0)),
                ('total_price', models.FloatField(default=0)),
                ('created', models.DateField(auto_now_add=True)),
                ('delivery_date', models.DateField()),
                ('delivered', models.BooleanField(default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('company_name', models.CharField(max_length=50)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='DZ')),
                ('address', models.CharField(max_length=100)),
                ('info', models.TextField(default='_', max_length=500)),
                ('debts', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0)])),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('phonenumber', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='DZ', unique=True)),
                ('username', models.CharField(max_length=200)),
                ('is_verified', models.BooleanField(default=False)),
                ('image', models.ImageField(default='images/account.jpg', null=True, upload_to='images/users')),
                ('location', django.contrib.gis.db.models.fields.PointField(default=django.contrib.gis.geos.point.Point(0, 0), srid=4326)),
                ('is_accepted', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
                ('user_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.usertype')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.CreateModel(
            name='CodeVerification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_verified', models.BooleanField(default=False)),
                ('code', models.IntegerField(validators=[django.core.validators.MinValueValidator(1000), django.core.validators.MaxValueValidator(9999)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('expires_at', models.DateTimeField(default=base.models.get_expiration_time)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DamagedProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('total_price', models.FloatField()),
                ('date', models.DateField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Clients_and_Products.product')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='DelievaryArrived',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delivered', models.BooleanField(default=False)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Human_Resources.employee')),
                ('output_receipt', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Receipts.output')),
            ],
        ),
        migrations.CreateModel(
            name='MediumTwo_Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('mediumtwo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.mediumtwo')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Clients_and_Products.product')),
            ],
        ),
        migrations.AddField(
            model_name='mediumtwo',
            name='products',
            field=models.ManyToManyField(through='base.MediumTwo_Products', to='Clients_and_Products.product'),
        ),
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=500)),
                ('title', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Product_Order_Envoy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_envoy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.orderenvoy')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Clients_and_Products.product')),
            ],
        ),
        migrations.AddField(
            model_name='orderenvoy',
            name='products',
            field=models.ManyToManyField(through='base.Product_Order_Envoy', to='Clients_and_Products.product'),
        ),
        migrations.CreateModel(
            name='Products_Medium',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(blank=True, null=True)),
                ('num_item', models.IntegerField(default=0)),
                ('total_price', models.FloatField(default=0)),
                ('medium', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.medium')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Clients_and_Products.product')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='medium',
            name='products',
            field=models.ManyToManyField(through='base.Products_Medium', to='Clients_and_Products.product'),
        ),
        migrations.CreateModel(
            name='ReturnedGoodsClient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('total_price', models.FloatField()),
                ('reason', models.CharField(blank=True, default=' ', max_length=50, null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Clients_and_Products.client')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Human_Resources.employee')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Clients_and_Products.product')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='ReturnedGoodsSupplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('total_price', models.FloatField()),
                ('reason', models.CharField(blank=True, default=' ', max_length=50, null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Human_Resources.employee')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Clients_and_Products.product')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.supplier')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]