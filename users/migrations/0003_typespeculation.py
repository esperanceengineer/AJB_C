# Generated by Django 4.1.3 on 2022-11-07 01:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_myuser_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeSpeculation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('active', models.BooleanField(default=False)),
                ('activite', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='speculations', to='users.typeactivte')),
            ],
        ),
    ]
