# Generated by Django 2.2 on 2021-07-20 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_wish_granted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wish_granted',
            name='grant_to',
        ),
        migrations.AddField(
            model_name='wish_granted',
            name='grant_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='granted', to='main.User'),
        ),
    ]