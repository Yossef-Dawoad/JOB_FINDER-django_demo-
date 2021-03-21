# Generated by Django 3.1.6 on 2021-03-21 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_job_jobtype'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='Experience',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='job',
            name='Salary',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='job',
            name='Vacancy',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='job',
            name='createdAt',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='job',
            name='descriptions',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
