# Generated by Django 3.1.2 on 2021-01-20 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0003_auto_20210120_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='itinerary',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tickets', to='ticket.itinerary'),
        ),
    ]