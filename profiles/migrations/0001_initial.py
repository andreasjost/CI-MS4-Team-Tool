# Generated by Django 3.0.6 on 2020-06-24 07:12

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('settings', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_id', models.CharField(editable=False, max_length=32)),
                ('company_name', models.CharField(blank=True, max_length=80, null=True)),
                ('street_address1', models.CharField(blank=True, max_length=80, null=True)),
                ('street_address2', models.CharField(blank=True, max_length=80, null=True)),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('postcode', models.CharField(blank=True, max_length=20, null=True)),
                ('town_or_city', models.CharField(blank=True, max_length=40, null=True)),
                ('plan', models.CharField(blank=True, max_length=40, null=True)),
                ('signup_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('renewal_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('payment', models.DecimalField(decimal_places=0, default=0, max_digits=2)),
                ('setting_daystart', models.DecimalField(decimal_places=0, default=0, max_digits=2)),
                ('setting_dayend', models.DecimalField(decimal_places=0, default=24, max_digits=2)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=80, null=True)),
                ('last_name', models.CharField(blank=True, max_length=80, null=True)),
                ('birthday_ddmm', models.CharField(default='0000', max_length=16)),
                ('start_date', models.DateField(default=datetime.date.today)),
                ('end_date', models.DateField(default=datetime.date.today)),
                ('level', models.CharField(choices=[('admin', 'Admin'), ('manager', 'Manager'), ('agent', 'Agent'), ('visitor', 'Visitor')], default='admin', max_length=16)),
                ('contract_type', models.CharField(choices=[('hour', 'Paid by the hour'), ('fix', 'Fix contract')], default='admin', max_length=16)),
                ('contract_percentage', models.DecimalField(decimal_places=0, default=0, max_digits=3)),
                ('agent_goal', models.CharField(blank=True, max_length=256, null=True)),
                ('company_id', models.CharField(editable=False, max_length=32)),
                ('role', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='agent_role', to='settings.AgentRole')),
                ('team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='team_member', to='settings.Team')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
