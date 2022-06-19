# Generated by Django 4.0.5 on 2022-06-19 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet_app', '0002_remove_pet_age_pet_born_pet_favorite_snack_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='pet',
            name='gender',
        ),
        migrations.AddField(
            model_name='pet',
            name='gender',
            field=models.ManyToManyField(to='pet_app.gender'),
        ),
    ]