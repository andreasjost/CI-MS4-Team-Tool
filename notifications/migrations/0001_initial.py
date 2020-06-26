# Generated by Django 3.0.6 on 2020-06-26 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0002_auto_20200626_1944'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_sender', models.CharField(max_length=80)),
                ('date', models.DateField()),
                ('message_text', models.CharField(max_length=200)),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='profiles.UserProfile')),
            ],
        ),
    ]
