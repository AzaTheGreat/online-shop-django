from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_method', models.CharField(choices=[('cash_courier', 'Cash to courier'),
                                                             ('card_courier', 'Card to courier'),
                                                             ('card_online', 'Card online')],
                                                    max_length=20, verbose_name='Payment method')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date of Creation')),
                ('status', models.CharField(choices=[('created', 'Created'), ('processing', 'Processing'),
                                                     ('shipped', 'Shipped'), ('delivered', 'Delivered'),
                                                     ('canceled', 'Canceled')],
                                            default='created', max_length=20, verbose_name='Status')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Quantity')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price')),
            ],
            options={
                'verbose_name': 'Ordered product',
                'verbose_name_plural': 'Ordered products',
            },
        ),
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Name')),
                ('last_name', models.CharField(max_length=50, verbose_name='Surname')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('phone', models.CharField(max_length=20, verbose_name='Phone Number')),
                ('address_line_1', models.CharField(max_length=200, verbose_name='Address')),
                ('address_line_2', models.CharField(blank=True, max_length=200, null=True,
                                                    verbose_name='Address (additional)')),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE,
                                               related_name='shipping_address', to='checkout.order',
                                               verbose_name='Order')),
            ],
            options={
                'verbose_name': 'Delivery address',
                'verbose_name_plural': 'Delivery addresses',
            },
        ),
    ]
