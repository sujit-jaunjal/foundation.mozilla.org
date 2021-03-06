# Generated by Django 2.2.17 on 2020-12-15 22:36

from django.db import migrations, models
from datetime import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailpages', '0022_auto_20201208_2004'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyersguidepage',
            name='cutoff_date',
            field=models.DateField(default=datetime(2020, 10, 29, 0, 0), help_text='Only show products that were reviewed on, or after this date.', verbose_name='Product listing cutoff date'),
        ),
    ]
