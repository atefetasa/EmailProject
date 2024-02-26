# Generated by Django 5.0.2 on 2024-02-21 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_module', '0005_alter_sitesettings_header_background_color_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesettings',
            name='header_background_color',
            field=models.CharField(blank=True, choices=[('#ffff66', 'light lime'), ('#ddccff', 'light purple'), ('#cce0ff', 'light blue'), ('#80ff80', 'light green'), ('#ffcccc', 'light red'), ('#99ebff', 'light sky blue'), ('white', 'white'), ('#f3ccff', 'pink purple')], default='#f3ccff', max_length=7),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='main_background_color',
            field=models.CharField(blank=True, choices=[('#ffff66', 'light lime'), ('#ddccff', 'light purple'), ('#cce0ff', 'light blue'), ('#80ff80', 'light green'), ('#ffcccc', 'light red'), ('#99ebff', 'light sky blue'), ('white', 'white'), ('#f3ccff', 'pink purple')], default='white', max_length=7),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='sidebar_background_color',
            field=models.CharField(blank=True, choices=[('#ffff66', 'light lime'), ('#ddccff', 'light purple'), ('#cce0ff', 'light blue'), ('#80ff80', 'light green'), ('#ffcccc', 'light red'), ('#99ebff', 'light sky blue'), ('white', 'white'), ('#f3ccff', 'pink purple')], default='white', max_length=7),
        ),
    ]
