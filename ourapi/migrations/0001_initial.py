# Generated by Django 5.1.4 on 2025-01-08 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('company_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('about', models.TextField()),
                ('type', models.CharField(choices=[('MNC', 'Multi National Company'), ('SME', 'Small Medium Enterprise'), ('Startup', 'Startup')], max_length=100)),
                ('added_date', models.DateField(auto_now_add=True)),
                ('activve', models.BooleanField(default=True)),
            ],
        ),
    ]