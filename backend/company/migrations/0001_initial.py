# Generated by Django 4.0.3 on 2022-03-18 17:28

import company.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyS',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(default='', max_length=500)),
                ('CIK_Number', models.CharField(default='', max_length=50, unique=True)),
                ('Ticket_Number', models.CharField(default='', max_length=50)),
                ('count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Performance',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('Growth', models.FloatField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('Profitability', models.FloatField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('Investibility', models.FloatField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('CompanyS', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.companys')),
            ],
        ),
        migrations.CreateModel(
            name='Metrics',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('Metric_Type', models.CharField(choices=[('Type1', 'GrowthRate'), ('Type2', 'CAC')], default='Type1', max_length=5)),
                ('Value', models.FloatField(default=0.0)),
                ('Source_Link', models.URLField()),
                ('Year', models.IntegerField(default=company.models.current_year, validators=[django.core.validators.MinValueValidator(2015), company.models.max_value_current_year], verbose_name='year')),
                ('Quarter', models.CharField(choices=[('1', '1st quarter'), ('2', '2nd quarter'), ('3', '3rd quarter'), ('4', '4th quarter')], default=1, max_length=1)),
                ('CompanyS', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.companys')),
            ],
        ),
        migrations.CreateModel(
            name='Forms',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('EDGAR_Link', models.URLField()),
                ('Form_Type', models.CharField(choices=[('10k', '10k'), ('10q', '10q'), ('8k', '8k')], default='10k', max_length=3)),
                ('CompanyS', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.companys')),
            ],
        ),
        migrations.CreateModel(
            name='CompFav',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('CompanyS', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.companys')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('CompanyS', 'account')},
            },
        ),
    ]