# Generated by Django 4.1.3 on 2022-11-08 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_myuser_fonction_myuser_personnes_charge_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='status',
            field=models.CharField(choices=[('En activité', 'En activité'), ('Au chômage', 'Au chômage'), ('Indisponible', 'Indisponible')], default='En activité', max_length=20, null=True),
        ),
    ]
