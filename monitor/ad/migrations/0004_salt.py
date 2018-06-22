# Generated by Django 2.0.1 on 2018-06-13 05:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0003_auto_20180611_1712'),
    ]

    operations = [
        migrations.CreateModel(
            name='Salt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=32)),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ad.UserInfo')),
            ],
        ),
    ]
