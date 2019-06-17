# Generated by Django 2.2.1 on 2019-06-12 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Username')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('address', models.CharField(max_length=100, verbose_name='Address')),
                ('message', models.CharField(max_length=500, verbose_name='Message')),
            ],
            options={
                'verbose_name': 'UserMessageContent',
            },
        ),
    ]