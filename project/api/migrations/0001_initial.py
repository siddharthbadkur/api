# Generated by Django 5.0.7 on 2024-07-30 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Studentapi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_name', models.CharField(max_length=45)),
                ('stu_email', models.EmailField(max_length=33)),
                ('stu_contact', models.IntegerField(verbose_name=20)),
                ('stu_city', models.CharField(max_length=50)),
            ],
        ),
    ]
