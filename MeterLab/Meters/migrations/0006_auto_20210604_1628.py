# Generated by Django 3.1.1 on 2021-06-04 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Meters', '0005_auto_20210604_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meterserials',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='meterserials_details',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
