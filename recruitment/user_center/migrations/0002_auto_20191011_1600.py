# Generated by Django 2.2.5 on 2019-10-11 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_center', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='name',
            field=models.CharField(max_length=20, null=True),
        ),
    ]