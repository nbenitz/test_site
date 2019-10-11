# Generated by Django 2.2.5 on 2019-10-11 03:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familia',
            fields=[
                ('id_familia', models.AutoField(primary_key=True, serialize=False)),
                ('apellido', models.CharField(max_length=20)),
                ('nro_cuenta', models.CharField(max_length=20)),
                ('direccion', models.CharField(blank=True, max_length=100, null=True)),
                ('telefono', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'familia',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id_familia', models.ForeignKey(db_column='id_familia', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='parcial.Familia')),
                ('nombre', models.CharField(max_length=20, unique=True)),
                ('ci', models.IntegerField()),
            ],
            options={
                'db_table': 'persona',
                'managed': False,
            },
        ),
    ]
