# Generated by Django 3.1.3 on 2020-12-05 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('post', models.AutoField(primary_key=True, serialize=False)),
                ('ten', models.TextField(blank=True, null=True)),
                ('link', models.TextField(blank=True, null=True)),
                ('photo', models.FileField(null=True, upload_to='')),
                ('theloai', models.CharField(max_length=100)),
            ],
        ),
    ]
