# Generated by Django 4.2.5 on 2024-01-30 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_alter_questions_options_alter_quizzes_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='img_path',
            field=models.TextField(blank=True, null=True, verbose_name='img_path'),
        ),
    ]
