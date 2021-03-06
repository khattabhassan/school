# Generated by Django 3.0.2 on 2022-02-03 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20220203_0518'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_Name', models.CharField(max_length=200)),
                ('student_Email', models.EmailField(max_length=200)),
                ('student_address', models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameField(
            model_name='school',
            old_name='School_Email',
            new_name='school_Email',
        ),
        migrations.RenameField(
            model_name='school',
            old_name='School_Name',
            new_name='school_Name',
        ),
        migrations.RenameField(
            model_name='school',
            old_name='School_address',
            new_name='school_address',
        ),
    ]
