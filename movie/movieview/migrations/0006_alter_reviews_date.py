# Generated by Django 4.0.1 on 2022-02-02 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieview', '0005_alter_reviews_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]