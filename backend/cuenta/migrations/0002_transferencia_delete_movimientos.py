# Generated by Django 4.2.7 on 2023-11-29 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuenta', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transferencia',
            fields=[
                ('transfer_id', models.AutoField(primary_key=True, serialize=False)),
                ('from_account_id', models.IntegerField(blank=True, null=True)),
                ('to_account_id', models.IntegerField(blank=True, null=True)),
                ('ammount', models.IntegerField(blank=True, null=True)),
                ('executed_at', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'transferencias',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Movimientos',
        ),
    ]