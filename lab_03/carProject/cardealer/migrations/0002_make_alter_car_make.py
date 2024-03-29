# Generated by Django 4.1.7 on 2023-04-17 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cardealer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Make',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='car',
            name='make',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cardealer.make'),
        ),
    ]
