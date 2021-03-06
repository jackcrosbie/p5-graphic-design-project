# Generated by Django 4.0.4 on 2022-05-27 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote_id', models.CharField(default='', editable=False, max_length=32)),
                ('name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=16, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('project_type', models.CharField(choices=[('custom', 'Custom'), ('website design', 'Website Design'), ('Maintenance', 'Maintenace'), ('Urgent Repair', 'Urgent Repair')], default='custom', max_length=20)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('deadline_date', models.CharField(max_length=20)),
                ('message', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Quotes',
            },
        ),
    ]
