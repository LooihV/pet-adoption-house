# Generated by Django 4.2.1 on 2023-05-12 01:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_breed_alter_role_employeeinformationid_species_pet'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adoption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Employee', to='index.user')),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.pet')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Adoptant', to='index.user')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.CharField(max_length=256)),
                ('adoption', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.adoption')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.event')),
            ],
        ),
    ]
