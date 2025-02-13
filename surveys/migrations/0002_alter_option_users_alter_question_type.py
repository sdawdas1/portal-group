# Generated by Django 5.1 on 2024-08-22 09:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='option',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='chosed_surveys_options', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='question',
            name='type',
            field=models.CharField(choices=[('single', 'Single choice'), ('multiple', 'Multiple choice')], default='single', max_length=25),
        ),
    ]
