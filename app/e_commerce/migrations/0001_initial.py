# Generated by Django 4.0.6 on 2022-07-10 12:06

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('mobile', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=75)),
                ('followers', models.IntegerField(default=0)),
                ('visitors', models.IntegerField(default=0)),
                ('size_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('height', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('cup_size', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('user_json', models.JSONField(blank=True, null=True)),
                ('human_parsing', models.ImageField(blank=True, null=True, upload_to='')),
                ('user_size', models.CharField(blank=True, max_length=7, null=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('gender', models.BooleanField(default=False)),
                ('user_model', models.TextField(blank=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_total', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=20, null=True)),
                ('shipping_charge', models.DecimalField(decimal_places=2, default=25, max_digits=5)),
                ('grand_total', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=20, null=True)),
                ('promo_code', models.CharField(default='NotCode', max_length=10)),
                ('promo_counter', models.IntegerField(default=0)),
                ('items_num', models.IntegerField(default=0)),
                ('cart_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_title', models.CharField(max_length=75)),
                ('category_gender', models.BooleanField(default=False)),
                ('category_description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CheckedCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_total', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('shipping_charge', models.DecimalField(decimal_places=2, max_digits=5)),
                ('grand_total', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('checked_cart_selling_date', models.DateField()),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_title', models.CharField(max_length=100)),
                ('product_details', models.TextField()),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product_discount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('product_brand', models.CharField(max_length=75)),
                ('total_quantity', models.IntegerField(default=0)),
                ('product_date_entry', models.DateField()),
                ('product_rating', models.DecimalField(decimal_places=1, default=0, max_digits=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('product_model', models.TextField(blank=True, null=True)),
                ('product_category', models.ManyToManyField(to='e_commerce.category')),
                ('product_vendor', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size_name', models.CharField(max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_rating', models.DecimalField(decimal_places=1, default=0, max_digits=5, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('review_content', models.TextField()),
                ('review_date', models.DateField()),
                ('review_product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='e_commerce.product')),
                ('review_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Quantity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('quantity_alarm', models.CharField(blank=True, max_length=100, null=True)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='e_commerce.product')),
                ('quantity_color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='e_commerce.color')),
                ('quantity_size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='e_commerce.size')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
                ('images_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='e_commerce.product')),
            ],
        ),
        migrations.CreateModel(
            name='CheckedCartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checked_cart_item_title', models.CharField(max_length=75)),
                ('checked_cart_item_photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('checked_cart_item_size', models.CharField(max_length=7)),
                ('checked_cart_item_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('checked_cart_item_quntity', models.IntegerField(default=1)),
                ('checked_cart', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='e_commerce.checkedcart')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='e_commerce.product')),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_item_size', models.CharField(max_length=7)),
                ('cart_item_color', models.CharField(max_length=7)),
                ('cart_item_quantity', models.IntegerField(default=1)),
                ('cart_item_title', models.CharField(blank=True, max_length=75, null=True)),
                ('cart_item_photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('cart_item_price', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('cart_item_cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='e_commerce.cart')),
                ('cart_item_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='e_commerce.product')),
            ],
        ),
    ]
