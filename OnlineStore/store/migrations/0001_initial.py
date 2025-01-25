from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='name')),
                ('slug', models.SlugField(allow_unicode=True, max_length=100, unique=True, verbose_name='slug')),
                ('image', models.ImageField(blank=True, upload_to='categories/', verbose_name='Image')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='TaggedItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.IntegerField(db_index=True, verbose_name='object ID')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                                   related_name='store_taggeditem_tagged_items',
                                                   to='contenttypes.contenttype', verbose_name='content type')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                          related_name='items',
                                          to='store.itemtag',
                                          verbose_name='Category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('slug', models.CharField(max_length=50, unique=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Publication date')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='New price')),
                ('old_price', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True,
                                                  verbose_name='Old price')),
                ('image', models.ImageField(blank=True, upload_to='items/', verbose_name='Image')),
                ('is_available', models.BooleanField(default=True, verbose_name='Available')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.',
                                                         related_name='tagged_items',
                                                         through='store.TaggedItem',
                                                         to='store.ItemTag',
                                                         verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Item',
                'verbose_name_plural': 'Items',
                'ordering': ['-price'],
            },
        ),
    ]
