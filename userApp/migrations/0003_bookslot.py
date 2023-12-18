# Generated by Django 3.2.10 on 2023-09-05 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0002_auto_20230810_1215'),
    ]

    operations = [
        migrations.CreateModel(
            name='bookslot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(blank=True, max_length=50, null=True)),
                ('lname', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('token', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
