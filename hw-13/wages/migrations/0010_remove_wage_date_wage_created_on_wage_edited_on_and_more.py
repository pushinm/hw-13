# Generated by Django 4.1.5 on 2023-01-24 21:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wages', '0009_alter_wage_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wage',
            name='date',
        ),
        migrations.AddField(
            model_name='wage',
            name='created_on',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата создания'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wage',
            name='edited_on',
            field=models.DateField(auto_now=True, verbose_name='Дата изменения'),
        ),
        migrations.AddField(
            model_name='wage',
            name='month',
            field=models.PositiveSmallIntegerField(choices=[(1, 1)], default='1', verbose_name='Месяц'),
        ),
        migrations.AddField(
            model_name='wage',
            name='year',
            field=models.PositiveSmallIntegerField(choices=[(1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023)], default=2023, verbose_name='Год'),
        ),
    ]
