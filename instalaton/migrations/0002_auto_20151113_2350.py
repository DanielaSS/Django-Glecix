# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('instalaton', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entrega',
            fields=[
                ('id_entrega', models.CharField(max_length=200, serialize=False, verbose_name=b'no de entrega', primary_key=True)),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('observaciones', models.CharField(max_length=200, null=True, verbose_name=b'Observaciones')),
                ('estado', models.CharField(max_length=200, null=True, verbose_name=b'Estado')),
            ],
        ),
        migrations.CreateModel(
            name='SODisponible',
            fields=[
                ('nombre', models.CharField(max_length=200, serialize=False, primary_key=True)),
                ('version', models.CharField(max_length=200, null=True)),
                ('arquitectura', models.CharField(max_length=200, null=True)),
                ('espacio_requerido_gb', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('documento', models.CharField(max_length=20, serialize=False, verbose_name=b'Documento', primary_key=True)),
                ('nombre', models.CharField(max_length=200, null=True, verbose_name=b'Nombre')),
                ('correo', models.CharField(max_length=100, null=True, verbose_name=b'Correo')),
                ('celular', models.IntegerField(default=0, verbose_name=b'Numero Celular')),
                ('tipoDocumento', models.CharField(max_length=4, verbose_name=b'Tipo Documento')),
                ('semestre', models.IntegerField(default=0, verbose_name=b'Semestre')),
                ('carrera', models.CharField(max_length=120, null=True, verbose_name=b'Carrera')),
                ('username', models.CharField(max_length=100, null=True, verbose_name=b'Nick')),
                ('contrasena', models.CharField(max_length=100, null=True, verbose_name=b'Contrasena')),
                ('rol', models.CharField(max_length=100, null=True, verbose_name=b'Rol')),
            ],
        ),
        migrations.AddField(
            model_name='equipo',
            name='backup',
            field=models.BooleanField(default=False, verbose_name=b'Backup'),
        ),
        migrations.AddField(
            model_name='equipo',
            name='caracteristicas',
            field=models.CharField(max_length=200, null=True, verbose_name=b'caracteristicas'),
        ),
        migrations.AddField(
            model_name='equipo',
            name='computador',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='equipo',
            name='contrasena',
            field=models.CharField(max_length=200, null=True, verbose_name=b'Contrasena'),
        ),
        migrations.AddField(
            model_name='equipo',
            name='espacioSO',
            field=models.IntegerField(default=0, verbose_name=b'Espacio Sistema Operativo'),
        ),
        migrations.AddField(
            model_name='equipo',
            name='marca',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='equipo',
            name='ram',
            field=models.IntegerField(default=0, verbose_name=b'RAM'),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='serial',
            field=models.CharField(max_length=200, serialize=False, verbose_name=b'Serial', primary_key=True),
        ),
        migrations.AddField(
            model_name='entrega',
            name='equipo',
            field=models.ForeignKey(related_name='Equipo', default=b'', to='instalaton.Equipo'),
        ),
        migrations.AddField(
            model_name='entrega',
            name='instalador',
            field=models.ForeignKey(related_name='instalador', default=b'', to='instalaton.Usuarios'),
        ),
        migrations.AddField(
            model_name='entrega',
            name='organizador',
            field=models.ForeignKey(related_name='Organizador', default=b'', to='instalaton.Usuarios'),
        ),
        migrations.AddField(
            model_name='entrega',
            name='usuario',
            field=models.ForeignKey(related_name='Dueno', default=b'', to='instalaton.Usuarios'),
        ),
        migrations.AddField(
            model_name='equipo',
            name='sOActual',
            field=models.ForeignKey(related_name='Sistema_Operativo_Actual', default=b'', to='instalaton.SODisponible'),
        ),
        migrations.AddField(
            model_name='equipo',
            name='sOFuturo',
            field=models.ForeignKey(related_name='Sistema_Operativo_Futuro', default=b'', to='instalaton.SODisponible'),
        ),
        migrations.AddField(
            model_name='equipo',
            name='usuario',
            field=models.ForeignKey(related_name='Usuario', default=b'', to='instalaton.Usuarios'),
        ),
    ]
