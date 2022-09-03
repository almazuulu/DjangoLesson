# Generated by Django 4.1 on 2022-09-01 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("newsapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="news",
            name="photo",
            field=models.ImageField(null=True, upload_to="photos/%Y/%m/%d"),
        ),
        migrations.AlterField(
            model_name="category",
            name="title_category",
            field=models.CharField(
                db_index=True, max_length=250, verbose_name="Имя категории"
            ),
        ),
        migrations.AlterField(
            model_name="news",
            name="category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="newsapp.category",
                verbose_name="Категория",
            ),
        ),
    ]
