# Generated by Django 2.1.7 on 2019-03-04 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20190303_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='interests',
            field=models.ManyToManyField(blank=True, related_name='interests', to='app.Interest', verbose_name='Интересы'),
        ),
    ]
