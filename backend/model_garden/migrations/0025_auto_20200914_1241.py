# Generated by Django 3.0.6 on 2020-09-14 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model_garden', '0024_auto_20200810_0335'),
    ]

    operations = [
        migrations.AddField(
            model_name='mediaasset',
            name='labeling_asset_filepath',
            field=models.CharField(default='', max_length=512),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='dataset_format',
            field=models.CharField(choices=[('PASCAL_VOC', 'Pascal VOC'), ('YOLO', 'YOLO')], default='PASCAL_VOC', max_length=16),
        ),
    ]
