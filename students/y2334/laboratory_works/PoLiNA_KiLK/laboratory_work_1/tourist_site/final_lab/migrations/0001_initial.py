# Generated by Django 3.1.2 on 2020-10-12 22:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buses',
            fields=[
                ('Number', models.IntegerField(primary_key=True, serialize=False, verbose_name='Номер автобуса')),
                ('Name', models.CharField(max_length=45, verbose_name='Название автобуса')),
                ('Total_run', models.IntegerField(null=True, verbose_name='Пробег')),
            ],
        ),
        migrations.CreateModel(
            name='Routes',
            fields=[
                ('Name', models.CharField(max_length=45, primary_key=True, serialize=False, verbose_name='Название пути')),
                ('Start', models.CharField(max_length=45, verbose_name='Точка старта')),
                ('Finish', models.CharField(max_length=45, verbose_name='Точка финиша')),
                ('Duration', models.IntegerField(verbose_name='Протяженность в километрах')),
            ],
        ),
        migrations.CreateModel(
            name='Ways',
            fields=[
                ('ID_way', models.AutoField(primary_key=True, serialize=False, verbose_name='Идентификатор маршрута')),
                ('Start_date', models.DateField(max_length=4, verbose_name='Дата начала поездки')),
                ('Finish_date', models.DateField(max_length=4, verbose_name='Дата конца поездки')),
                ('Passengers', models.IntegerField(verbose_name='Колличество пасажиров')),
                ('Ticket_cost', models.IntegerField(verbose_name='Стоимость билета')),
                ('Done_flag', models.BooleanField(default=False, verbose_name='Статус завершенности')),
                ('Name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='name', to='final_lab.routes')),
                ('Number', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='number', to='final_lab.buses')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('Table_number', models.AutoField(primary_key=True, serialize=False, verbose_name='Табличный номер')),
                ('Experience', models.IntegerField(null=True, verbose_name='Стаж вождения')),
                ('Category', models.CharField(choices=[('A', 'Мотоциклы'), ('A1', 'Легкие мотоциклы'), ('B', 'Легкие автомобили'), ('B1', 'Трициклы и квадроциклы'), ('C', 'Грузовики'), ('C1', 'Грузовики'), ('D', 'Автобусы'), ('D1', 'Автобусы'), ('BE', 'Владение легковесным прицепом'), ('CE', 'Владение тяжеловесным прицепом'), ('C1E', 'Грузовики подкатегории C1'), ('DE', 'Автобусы с прицепом'), ('D1E', 'Автобусы подкатегории D1'), ('M', 'Мопеды и квадроциклы'), ('Tm', 'Трамваи'), ('Tb', 'Троллейбусы')], max_length=3, verbose_name='Типы транспорта')),
                ('Address', models.CharField(max_length=50, verbose_name='Адрес проживания')),
                ('Birth_year', models.DateField(max_length=4, verbose_name='Год рождения')),
                ('Second_name', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('Number', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='number_bus', to='final_lab.buses')),
            ],
        ),
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('ID_TR', models.AutoField(primary_key=True, serialize=False, verbose_name='Идентификатор пути')),
                ('Towns', models.CharField(max_length=30, verbose_name='Город')),
                ('Name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Name_route', to='final_lab.routes')),
            ],
        ),
    ]