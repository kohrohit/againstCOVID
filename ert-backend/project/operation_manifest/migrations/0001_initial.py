# Generated by Django 2.2.1 on 2020-04-21 20:40

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import djchoices.choices


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'country',
            },
        ),
        migrations.CreateModel(
            name='DailyLimit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('count', models.IntegerField()),
            ],
            options={
                'db_table': 'daily_limit',
            },
        ),
        migrations.CreateModel(
            name='Forex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('currency', models.CharField(choices=[('USD', 'USD')], default='USD', max_length=3, validators=[djchoices.choices.ChoicesValidator({'USD': 'USD'})])),
                ('inr_rate', models.FloatField()),
            ],
            options={
                'db_table': 'forex',
            },
        ),
        migrations.CreateModel(
            name='IndianState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(choices=[('AN', 'ANDAMAN AND NICOBAR'), ('AP', 'ANDRA PRADESH'), ('AR', 'ARUNACHAL PRADESH'), ('AS', 'ASSAM'), ('BR', 'BIHAR'), ('CT', 'CHHATTISGARH'), ('CH', 'CHANDIGARH'), ('DD', 'DAMAN AND DIU'), ('DL', 'DELHI'), ('DN', 'DADRA AND NAGAR HAVELI'), ('GA', 'GOA'), ('GJ', 'GUJARAT'), ('HR', 'HARYANA'), ('HP', 'HIMACHAL PRADESH'), ('JH', 'JHARKHAND'), ('JK', 'JAMMU AND KASHMIR'), ('KA', 'KARNATAKA'), ('KL', 'KERALA'), ('LD', 'LAKSHADWEEP'), ('MH', 'MAHARASHTRA'), ('MP', 'MADHYA PRADESH'), ('MZ', 'MIZORAM'), ('NL', 'NAGALAND'), ('OD', 'ODISHA'), ('PB', 'PUNJAB'), ('PY', 'PUDUCHERRY'), ('RJ', 'RAJASTHAN'), ('SK', 'SIKKIM'), ('TN', 'TAMIL NADU'), ('TR', 'TRIPURA'), ('TS', 'TELANGANA'), ('UK', 'UTTARAKHAND'), ('UP', 'UTTAR PRADESH'), ('WB', 'WEST BENGAL')], max_length=3, validators=[djchoices.choices.ChoicesValidator({'AN': 'ANDAMAN AND NICOBAR', 'AP': 'ANDRA PRADESH', 'AR': 'ARUNACHAL PRADESH', 'AS': 'ASSAM', 'BR': 'BIHAR', 'CH': 'CHANDIGARH', 'CT': 'CHHATTISGARH', 'DD': 'DAMAN AND DIU', 'DL': 'DELHI', 'DN': 'DADRA AND NAGAR HAVELI', 'GA': 'GOA', 'GJ': 'GUJARAT', 'HP': 'HIMACHAL PRADESH', 'HR': 'HARYANA', 'JH': 'JHARKHAND', 'JK': 'JAMMU AND KASHMIR', 'KA': 'KARNATAKA', 'KL': 'KERALA', 'LD': 'LAKSHADWEEP', 'MH': 'MAHARASHTRA', 'MP': 'MADHYA PRADESH', 'MZ': 'MIZORAM', 'NL': 'NAGALAND', 'OD': 'ODISHA', 'PB': 'PUNJAB', 'PY': 'PUDUCHERRY', 'RJ': 'RAJASTHAN', 'SK': 'SIKKIM', 'TN': 'TAMIL NADU', 'TR': 'TRIPURA', 'TS': 'TELANGANA', 'UK': 'UTTARAKHAND', 'UP': 'UTTAR PRADESH', 'WB': 'WEST BENGAL'})])),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'indian_state',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('place_id', models.CharField(blank=True, max_length=200)),
                ('geo_coordinates', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
                ('pin_code', models.CharField(blank=True, max_length=10)),
                ('address', models.TextField(blank=True, max_length=300)),
                ('landmark', models.TextField(blank=True, null=True)),
                ('location', models.TextField(blank=True, null=True)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('icon', models.URLField(blank=True, max_length=120, null=True)),
                ('image', models.URLField(blank=True, max_length=120, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='operation_manifest.Country')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='operation_manifest.IndianState')),
            ],
            options={
                'db_table': 'city',
            },
        ),
    ]
