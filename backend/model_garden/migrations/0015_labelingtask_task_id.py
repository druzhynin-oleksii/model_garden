# Generated by Django 3.0.6 on 2020-05-20 21:02

from django.db import migrations, models


def set_task_id(apps, schema_editor):
    LabelingTask = apps.get_model('model_garden', 'LabelingTask')
    for labeling_task in LabelingTask.objects.all().iterator():
        if labeling_task.url:
            labeling_task.task_id = labeling_task.url.split('/')[-1]
            labeling_task.save()
        else:
            labeling_task.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('model_garden', '0014_labelingtask_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='labelingtask',
            name='task_id',
            field=models.IntegerField(null=True),
            preserve_default=False,
        ),
        migrations.RunPython(set_task_id, lambda apps, schema_editor: None),
    ]
