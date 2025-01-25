from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback_name', models.CharField(max_length=50, verbose_name='Customer Name')),
                ('feedback_email', models.EmailField(max_length=254, verbose_name='Customer email')),
                ('feedback_message', models.TextField(verbose_name='Message')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date of creation')),
            ],
            options={
                'verbose_name': 'Customers Feedback',
                'verbose_name_plural': 'Customer Feedback',
            },
        ),
    ]
