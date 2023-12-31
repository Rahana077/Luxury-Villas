# Generated by Django 3.2.10 on 2023-08-10 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userregistrationdb',
            old_name='U_mobile',
            new_name='umob',
        ),
        migrations.RemoveField(
            model_name='userregistrationdb',
            name='U_email',
        ),
        migrations.RemoveField(
            model_name='userregistrationdb',
            name='U_name',
        ),
        migrations.RemoveField(
            model_name='userregistrationdb',
            name='U_pswd',
        ),
        migrations.AddField(
            model_name='userregistrationdb',
            name='uemail',
            field=models.EmailField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='userregistrationdb',
            name='uimg',
            field=models.ImageField(blank=True, null=True, upload_to='profile pic'),
        ),
        migrations.AddField(
            model_name='userregistrationdb',
            name='uname',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='userregistrationdb',
            name='upass',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
